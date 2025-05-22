from flask import Flask, request, send_file, render_template
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import os
from io import BytesIO

app = Flask(__name__)

# Tạo khóa AES 32 byte từ chuỗi bất kỳ
def get_aes_key(key_str):
    return SHA256.new(key_str.encode()).digest()  # AES 256-bit

# Mã hóa file
def encrypt_file(file_data, key):
    key_bytes = get_aes_key(key)
    iv = get_random_bytes(16)
    cipher = AES.new(key_bytes, AES.MODE_CFB, iv=iv)
    encrypted_data = iv + cipher.encrypt(file_data)
    return encrypted_data

# Giải mã file
def decrypt_file(file_data, key):
    key_bytes = get_aes_key(key)
    iv = file_data[:16]
    encrypted_content = file_data[16:]
    cipher = AES.new(key_bytes, AES.MODE_CFB, iv=iv)
    decrypted_data = cipher.decrypt(encrypted_content)
    return decrypted_data

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_file():
    uploaded_file = request.files.get("file")
    key = request.form.get("key")
    action = request.form.get("action")

    if not uploaded_file or not key or not action:
        return "Thiếu dữ liệu", 400

    file_data = uploaded_file.read()

    try:
        if action == "encrypt":
            result_data = encrypt_file(file_data, key)
            filename = uploaded_file.filename + ".enc"
        elif action == "decrypt":
            result_data = decrypt_file(file_data, key)
            filename = uploaded_file.filename + ".dec"
        else:
            return "Thao tác không hợp lệ", 400

        # Trả file kết quả về cho client
        return send_file(
            BytesIO(result_data),
            as_attachment=True,
            download_name=filename,
            mimetype="application/octet-stream"
        )
    except Exception as e:
        print("Lỗi xử lý:", str(e))
        return "Lỗi trong quá trình xử lý", 500

if __name__ == "__main__":
    app.run(debug=True)
