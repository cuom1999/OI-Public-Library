# Quy ước dịch thuật

Mục tiêu của lớp `vi/` là tạo nguồn LaTeX tiếng Việt nhất quán cho các tài
liệu trong OI Public Library, kể cả những tệp gốc chỉ có PDF.

## Nguyên tắc chung

- Giữ nguyên tệp gốc. Bản dịch đặt trong `vi/sources/` theo nhóm chủ đề tương
  ứng, ví dụ `vi/sources/graph-theory/`.
- Mỗi tài liệu dịch là một tệp LaTeX độc lập và được biên dịch riêng thành
  PDF.
- Đầu mỗi tệp dịch nên có dòng chú thích `% Source-PDF: <đường/dẫn/gốc.pdf>`
  hoặc `% Source-File: <đường/dẫn/gốc>` để manifest tự động nhận diện trạng
  thái dịch.
- Dùng LuaLaTeX và `oipl-vn.sty` cho font, lề trang, liên kết, danh sách và
  ký hiệu toán học.
- Bảo toàn công thức, ký hiệu, độ phức tạp thuật toán và cấu trúc chung của
  bài gốc.
- Code, tên hàm, tên biến, tên bài thi và tên thuật toán thông dụng được giữ
  bằng tiếng Anh khi đó là cách gọi quen thuộc trong cộng đồng lập trình thi
  đấu.
- Chỉ thêm tên tiếng Anh trong ngoặc khi thuật ngữ đó hữu ích để tra cứu, ví
  dụ: "thành phần liên thông mạnh (strongly connected component)".

## Xử lý PDF-only

1. Dùng `pdfinfo` để ghi nhận số trang và metadata có ích.
2. Thử `pdftotext -layout <file.pdf> -` trước. Nếu văn bản rõ, chuyển thành
   LaTeX thủ công và dịch.
3. Nếu văn bản bị vỡ dòng, mất công thức hoặc PDF là ảnh scan, tạo nguồn
   LaTeX theo nội dung đọc được tốt nhất và để lại ghi chú trong đầu tệp.
4. Không cố gắng tái tạo bố cục pixel-perfect; ưu tiên nguồn LaTeX sạch, dễ
   đọc, nhất quán và biên dịch được.
5. Sau khi thêm hoặc sửa tệp trong `vi/sources/`, chạy `make` từ thư mục
   `vi/` và sửa lỗi biên dịch trước khi coi bản dịch là xong.

## Trạng thái hiện tại

- `sources/graph-theory/2-sat.tex`: dịch từ PDF "2-SAT 解法浅析" của Zhao
  Shuang, 3 trang.
