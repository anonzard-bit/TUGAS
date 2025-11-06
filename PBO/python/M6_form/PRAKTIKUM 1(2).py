# Form login
print("Sistem Aplikasi Perpustakaan Sekolah")
print("================== FORM LOGIN ==================")
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")
input_privilege = input("Masukkan Hak akses/Privilage: ")
print("================================================")

# Validasi langsung dengan if
if input_username == "rplskaneda":
    if input_password == "12345":
        if input_privilege == "admin":
            print("Login berhasil ..")
            print("Anda Sebagai", input_privilege)
        else:
            print("Login gagal. Hak Akses/Privilage Salah")
            print("Anda Sebagai", input_privilege)
    else:
        print("Login gagal. Password Salah")
        print("Anda Sebagai", input_privilege)
else:
    print("Login gagal. Username Salah")
    print("Anda Sebagai", input_privilege)