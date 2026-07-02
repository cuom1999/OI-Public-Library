#!/usr/bin/env python3
"""Extract readable text from old binary Word .doc files without olefile.

This is intentionally small and only implements the Compound File pieces needed
by the Word 9 documents in this archive: read WordDocument plus the 0Table or
1Table stream, then decode the CLX piece table.
"""

from __future__ import annotations

import re
import struct
import sys
from pathlib import Path

ENDOFCHAIN = 0xFFFFFFFE
FREESECT = 0xFFFFFFFF


class CompoundFile:
    def __init__(self, path: Path) -> None:
        self.data = path.read_bytes()
        if self.data[:8] != b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1":
            raise ValueError("not a Compound File Binary document")

        self.sector_size = 1 << struct.unpack_from("<H", self.data, 0x1E)[0]
        self.mini_size = 1 << struct.unpack_from("<H", self.data, 0x20)[0]
        self.num_fat = struct.unpack_from("<I", self.data, 0x2C)[0]
        self.first_dir = struct.unpack_from("<I", self.data, 0x30)[0]
        self.mini_cutoff = struct.unpack_from("<I", self.data, 0x38)[0]
        self.first_minifat = struct.unpack_from("<I", self.data, 0x3C)[0]
        self.num_minifat = struct.unpack_from("<I", self.data, 0x40)[0]

        difat = struct.unpack_from("<109I", self.data, 0x4C)
        fat_sectors = [x for x in difat if x not in (FREESECT, ENDOFCHAIN)]
        self.fat: list[int] = []
        for sid in fat_sectors[: self.num_fat]:
            off = self._sector_offset(sid)
            self.fat.extend(struct.unpack_from(f"<{self.sector_size // 4}I", self.data, off))

        self.entries: dict[str, tuple[int, int, int]] = {}
        self.root_stream = b""
        self._read_directory()
        self.minifat: list[int] = []
        self._read_minifat()

    def _sector_offset(self, sid: int) -> int:
        return (sid + 1) * self.sector_size

    def _chain(self, start: int, table: list[int] | None = None) -> list[int]:
        links = self.fat if table is None else table
        out: list[int] = []
        seen: set[int] = set()
        sid = start
        while sid not in (ENDOFCHAIN, FREESECT) and sid < len(links) and sid not in seen:
            seen.add(sid)
            out.append(sid)
            sid = links[sid]
        return out

    def _read_sector_chain(self, start: int, size: int | None = None) -> bytes:
        raw = b"".join(
            self.data[self._sector_offset(sid) : self._sector_offset(sid) + self.sector_size]
            for sid in self._chain(start)
        )
        return raw if size is None else raw[:size]

    def _read_directory(self) -> None:
        directory = self._read_sector_chain(self.first_dir)
        root_start = root_size = 0
        for off in range(0, len(directory), 128):
            entry = directory[off : off + 128]
            if len(entry) < 128:
                break
            name_len = struct.unpack_from("<H", entry, 64)[0]
            if name_len < 2:
                continue
            name = entry[: name_len - 2].decode("utf-16le", errors="ignore")
            typ = entry[66]
            start = struct.unpack_from("<I", entry, 116)[0]
            size = struct.unpack_from("<Q", entry, 120)[0]
            self.entries[name] = (typ, start, size)
            if typ == 5:
                root_start, root_size = start, size
        if root_size:
            self.root_stream = self._read_sector_chain(root_start, root_size)

    def _read_minifat(self) -> None:
        if self.first_minifat == FREESECT:
            return
        for sid in self._chain(self.first_minifat)[: self.num_minifat]:
            off = self._sector_offset(sid)
            self.minifat.extend(struct.unpack_from(f"<{self.sector_size // 4}I", self.data, off))

    def read_stream(self, name: str) -> bytes:
        _typ, start, size = self.entries[name]
        if size < self.mini_cutoff and self.minifat:
            raw = b"".join(
                self.root_stream[sid * self.mini_size : (sid + 1) * self.mini_size]
                for sid in self._chain(start, self.minifat)
            )
            return raw[:size]
        return self._read_sector_chain(start, size)


def extract_doc_text(path: Path) -> str:
    ole = CompoundFile(path)
    word = ole.read_stream("WordDocument")
    flags = struct.unpack_from("<H", word, 0x0A)[0]
    table_name = "1Table" if flags & 0x0200 else "0Table"
    table = ole.read_stream(table_name)
    fc_clx, lcb_clx = struct.unpack_from("<II", word, 0x01A2)
    clx = table[fc_clx : fc_clx + lcb_clx]

    pos = 0
    pieces: list[str] = []
    while pos < len(clx):
        tag = clx[pos]
        pos += 1
        if tag == 1:
            size = struct.unpack_from("<H", clx, pos)[0]
            pos += 2 + size
            continue
        if tag != 2:
            break
        size = struct.unpack_from("<I", clx, pos)[0]
        pos += 4
        pcdt = clx[pos : pos + size]
        count = (size - 4) // 12
        cps = [struct.unpack_from("<I", pcdt, 4 * i)[0] for i in range(count + 1)]
        pcd_start = 4 * (count + 1)
        for i in range(count):
            cp0, cp1 = cps[i], cps[i + 1]
            pcd = pcdt[pcd_start + 8 * i : pcd_start + 8 * (i + 1)]
            fc = struct.unpack_from("<I", pcd, 2)[0]
            compressed = bool(fc & 0x40000000)
            offset = fc & 0x3FFFFFFF
            chars = cp1 - cp0
            if compressed:
                raw = word[offset // 2 : offset // 2 + chars]
                pieces.append(raw.decode("gbk", errors="ignore"))
            else:
                raw = word[offset : offset + chars * 2]
                pieces.append(raw.decode("utf-16le", errors="ignore"))
        break

    text = "".join(pieces).replace("\r", "\n")
    text = re.sub(r"\x13[^\x14\x15]*(?:\x14)?", "", text).replace("\x15", "")
    for ch in ["\x00", "\x07", "\x08", "\x0b", "\x0c"]:
        text = text.replace(ch, "")
    return re.sub(r"\n{3,}", "\n\n", text)


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} SOURCE.doc", file=sys.stderr)
        return 2
    print(extract_doc_text(Path(sys.argv[1])), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
