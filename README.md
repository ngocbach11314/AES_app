# AES File Encryptor / Decryptor Web

Trang web đơn giản cho phép người dùng mã hóa và giải mã file sử dụng thuật toán AES. Giao diện web được xây dựng bằng HTML, CSS (Bootstrap), JavaScript, và xử lý mã hóa/giải mã trên server bằng Flask (Python).

---

## Tính năng

- Chọn file để mã hóa hoặc giải mã.
- Nhập khóa mã hóa/giải mã dưới dạng chuỗi hoặc hex.
- Ẩn/hiện khóa nhập để tăng tính bảo mật khi nhập.
- Gửi file và khóa lên server Flask xử lý AES.
- Tải file kết quả mã hóa/giải mã về máy.

---

## Công nghệ sử dụng

- Frontend:
  - HTML5
  - CSS (Bootstrap 5)
  - JavaScript (Fetch API)
- Backend:
  - Python 3
  - Flask
  - Thư viện mã hóa AES (ví dụ: `pycryptodome`)

---
## Giao diện
![image](https://github.com/user-attachments/assets/f02e5597-6055-42bb-a8e1-2459bd54691a)
![image](https://github.com/user-attachments/assets/3f9d1ffc-af72-4f83-a975-c94ae1397f2f)

## Cấu trúc
project_root
  - templates
     + index.html
  - static
     + style.css
  - app.py
  - README.md

Nghiêm Thị Ngọc Bích 
CNTT 17-07
http://127.0.0.1:5000


