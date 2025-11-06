# Form login
print("Sistem Aplikasi Perpustakaan Sekolah")
print("================== FORM LOGIN ==================")
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")
input_privilege = input("Masukkan Hak akses/Privilage: ")
print("================================================")

# Validasi dengan if-elif-else
if input_username != "rplskaneda":
    print("Login gagal. Username Salah")
    print("Anda Sebagai", input_privilege)
elif input_password != "12345":
    print("Login gagal. Password Salah")
    print("Anda Sebagai", input_privilege)
elif input_privilege != "admin":
    print("Login gagal. Hak Akses/Privilage Salah")
    print("Anda Sebagai", input_privilege)
else:
    print("Login berhasil ..")
    print("Anda Sebagai", input_privilege)