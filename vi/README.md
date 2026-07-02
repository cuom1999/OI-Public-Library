# Thư viện OI Public Library tiếng Việt

Thư mục này chứa lớp bản dịch tiếng Việt cho
`enkerewpo/OI-Public-Library`. Các tệp gốc được giữ nguyên ở các thư mục
thượng nguồn; bản dịch LaTeX mới được đặt trong `vi/sources/` và dùng chung
gói định dạng `vi/oipl-vn.sty`.

## Biên dịch

Can LuaLaTeX. Tu thu muc `vi/`, chay:

```sh
make
```

Makefile tự động tìm mọi tệp `sources/**/*.tex` và biên dịch mỗi tệp thành PDF
tương ứng trong `build/`.

## Cách tổ chức

- `sources/`: nguồn LaTeX tiếng Việt.
- `build/`: PDF sinh ra khi biên dịch, không viết tay.
- `oipl-vn.sty`: định dạng chung cho tất cả bản dịch.
- `TRANSLATION.md`: quy ước dịch thuật và quy trình xử lý PDF-only.
- `QUALITY_AUDIT.md`: danh sách các tệp đã có bản LaTeX nhưng chưa đủ chất
  lượng hoặc mới là ghi chú mục lục/tóm tắt.
- `QUALITY_WORKLIST.md`: hàng đợi chi tiết theo từng bài trong các tuyển tập
  dài; sinh bằng `tools/build_quality_worklist.py`.
