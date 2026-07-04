#!/usr/bin/env python3
"""Build a translation manifest for the Vietnamese OI Public Library fork."""

from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VI = ROOT / "vi"
OUT = VI / "MANIFEST.md"
TODO = VI / "TODO.md"
TRACKED_EXTS = {
    ".pdf": "pdf",
    ".doc": "doc",
    ".docx": "docx",
    ".ppt": "ppt",
    ".pptx": "pptx",
    ".rtf": "rtf",
    ".md": "md",
}
SKIP_PREFIXES = ("vi/", ".git/")
REFERENCE_NOTE_SOURCES = {
    "英文资料 ENGLISH MATERIALS/Introduction To Algorithm - 3rd Edition.pdf",
    "英文资料 ENGLISH MATERIALS/Computer Systems, A Programmer’s Perspective 3rd Edition.pdf",
    "英文资料 ENGLISH MATERIALS/Concrete Mathematics - 2nd Edition.pdf",
    "英文资料 ENGLISH MATERIALS/A Probability Path - Resnick.pdf",
    "英文资料 ENGLISH MATERIALS/Data Structures and Network Algorithms - Tarjan [1987-01-01].pdf",
    "USACO/【由 BirDOR 整理】USACO 2001-2007 月赛测试数据+题目+题解/USACO月赛十年题典v10.pdf",
    "其他 OTHERS/一份不太简短的LATEX介绍.pdf",
}
COMPANION_NOTE_SOURCES = {
    "IOI中国国家候选队论文/2001/刘汝佳(不完整).pdf",
    "USACO/USACO题解(NOCOW整理版)47P.pdf",
    "动态规划 DYNAMIC PROGRAMMING/树形DP选讲 - 顾逸宏.pdf",
    "动态规划 DYNAMIC PROGRAMMING/初探数位dp.pdf",
    "数据结构 DATA STRUCTURE/Link Cut Trees.pdf",
    "图论 GRAPH THEORY/Making Graphs into Trees - immortalCO, WrongAnswer.pdf",
    "图论 GRAPH THEORY/经典网络流教程.pdf",
    "图论 GRAPH THEORY/区间图、弦图和完美图.pdf",
    "英文资料 ENGLISH MATERIALS/Game Theory - Thomas S. Ferguson.pdf",
    "数据结构 DATA STRUCTURE/后缀自动机 - 陈立杰.pdf",
    "其他 OTHERS/C++的pb-ds库在OI中的应用 - 于纪平.pdf",
    "其他 OTHERS/CDQ分治入门经典.pdf",
    "其他 OTHERS/NOI2016-旷野大计算-题解.pdf",
    "其他 OTHERS/博弈论相关 - 李晓潇.pdf",
}
CODE_TEMPLATE_SOURCES = {
    "模板 TEMPLATES/HEOI2018模板复习手册 - Kvar_ispw17.pdf",
    "模板 TEMPLATES/Macac_rio_Maratona_de_Programa__o.pdf",
    "模板 TEMPLATES/NOIP2017模板复习手册 - Kvar_ispw17.pdf",
    "模板 TEMPLATES/chota1219.pdf",
    "模板 TEMPLATES/kuangbin的ACM模板（新）.pdf",
    "模板 TEMPLATES/上海交通大学ACM模板.pdf",
    "模板 TEMPLATES/吉林大学ACM模板.pdf",
    "模板 TEMPLATES/计算几何模板 - 吉如一.md",
    "模板 TEMPLATES/计算几何模板-HIT.pdf",
}


def git_files() -> list[str]:
    raw = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    return [p for p in raw.decode("utf-8", errors="replace").split("\0") if p]


def page_count(path: str) -> str:
    if not path.lower().endswith(".pdf"):
        return ""
    try:
        out = subprocess.check_output(
            ["pdfinfo", path],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "?"
    match = re.search(r"^Pages:\s+(\d+)", out, re.MULTILINE)
    return match.group(1) if match else "?"


def translated_sources() -> dict[str, str]:
    result: dict[str, str] = {}
    pattern = re.compile(r"^%\s+Source-(?:PDF|File):\s+(.+?)\s*$", re.MULTILINE)
    for tex in sorted((VI / "sources").glob("**/*.tex")):
        text = tex.read_text(encoding="utf-8", errors="replace")
        for match in pattern.finditer(text):
            result[match.group(1)] = str(tex.relative_to(ROOT))
    return result


def rows() -> list[dict[str, str]]:
    translated = translated_sources()
    data: list[dict[str, str]] = []
    for path in git_files():
        if path.startswith(SKIP_PREFIXES):
            continue
        ext = Path(path).suffix.lower()
        kind = TRACKED_EXTS.get(ext)
        if not kind:
            continue
        if path in translated:
            if path in REFERENCE_NOTE_SOURCES:
                status = "reference-note"
            elif path in CODE_TEMPLATE_SOURCES:
                status = "code-template"
            elif path in COMPANION_NOTE_SOURCES:
                status = "companion-note"
            else:
                status = "translated"
        else:
            status = "todo"
        data.append(
            {
                "status": status,
                "kind": kind,
                "pages": page_count(path),
                "source": path,
                "translation": translated.get(path, ""),
            }
        )
    status_order = {
        "todo": 0,
        "reference-note": 1,
        "code-template": 2,
        "companion-note": 3,
        "translated": 4,
    }
    data.sort(key=lambda r: (status_order.get(r["status"], 99), r["kind"], r["source"]))
    return data


def write_manifest(data: list[dict[str, str]]) -> None:
    counts: dict[str, int] = {}
    for row in data:
        counts[row["kind"]] = counts.get(row["kind"], 0) + 1
    translated = sum(1 for row in data if row["status"] == "translated")
    reference_notes = sum(1 for row in data if row["status"] == "reference-note")
    code_templates = sum(1 for row in data if row["status"] == "code-template")
    companion_notes = sum(1 for row in data if row["status"] == "companion-note")
    todo = sum(1 for row in data if row["status"] == "todo")

    lines = [
        "# Vietnamese Translation Manifest",
        "",
        "Generated by `vi/tools/build_manifest.py`.",
        "",
        f"- Tracked source documents: {len(data)}",
        f"- Translated documents: {translated}",
        f"- Reference-note documents: {reference_notes}",
        f"- Code-template documents: {code_templates}",
        f"- Companion-note documents: {companion_notes}",
        f"- Remaining documents: {todo}",
        "",
        "## Counts By Type",
        "",
        "| Type | Count |",
        "| --- | ---: |",
    ]
    for kind in sorted(counts):
        lines.append(f"| {kind} | {counts[kind]} |")

    lines.extend(
        [
            "",
            "## Documents",
            "",
            "| Status | Type | Pages | Source | Translation |",
            "| --- | --- | ---: | --- | --- |",
        ]
    )
    for row in data:
        lines.append(
            "| {status} | {kind} | {pages} | `{source}` | {translation} |".format(
                status=row["status"],
                kind=row["kind"],
                pages=row["pages"],
                source=row["source"].replace("|", r"\|"),
                translation=f"`{row['translation']}`" if row["translation"] else "",
            )
        )
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    csv_path = VI / "MANIFEST.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["status", "kind", "pages", "source", "translation"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(data)

    short_pdfs = [
        row
        for row in data
        if row["status"] == "todo"
        and row["kind"] == "pdf"
        and row["pages"].isdigit()
        and int(row["pages"]) <= 10
    ]
    short_pdfs.sort(key=lambda r: (int(r["pages"]), r["source"]))

    todo_lines = [
        "# Translation Work Queue",
        "",
        "Generated by `vi/tools/build_manifest.py`.",
        "",
        "Quality issues for files that already have a LaTeX translation are tracked",
        "separately in `QUALITY_AUDIT.md`.",
        "",
        "## Short PDF-first Queue",
        "",
        "These PDF-only documents are at most 10 pages and are good candidates for",
        "parallel subagent translation.",
        "",
        "| Pages | Source |",
        "| ---: | --- |",
    ]
    for row in short_pdfs:
        todo_lines.append(f"| {row['pages']} | `{row['source'].replace('|', r'\|')}` |")

    TODO.write_text("\n".join(todo_lines) + "\n", encoding="utf-8")


def main() -> None:
    write_manifest(rows())


if __name__ == "__main__":
    main()
