print("Sistem Aplikasi Perpustakaan Sekolah")
print("================== FORM LOGIN ==================")
u = input("Masukkan username: ")
p = input("Masukkan password: ")
h = input("Masukkan Hak akses/Privilage: ")
print("================================================")
if u == "rplskaneda" and p == "12345" and h == "admin":
    print("Login berhasil ..")
    print("Anda Sebagai", h)
else:
    print("Login gagal.")