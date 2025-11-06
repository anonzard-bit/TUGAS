# Program Form Login Sederhana

# Input data login
username = input("Masukkan username: ")
password = input("Masukkan password: ")

# Proses validasi
if username == "admin" and password == "12345":
    print("Login berhasil! Selamat datang,", username)
else:
    print("Login gagal! Username atau password salah.")
