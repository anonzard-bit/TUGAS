# Data akses yang tersimpan
user_data = {
    'username': 'rplskaneda',
    'password': '12345',
    'privilege': 'admin'
}

def check_login(username, password, privilege):
    # Memeriksa kecocokan username
    if username != user_data['username']:
        return False, "Username"
    
    # Memeriksa kecocokan password
    if password != user_data['password']:
        return False, "Password"
    
    # Memeriksa kecocokan hak akses
    if privilege != user_data['privilege']:
        return False, "Hak Akses/Privilage"
    
    # Jika semua data cocok
    return True, "Berhasil"

# Form login
print("Sistem Aplikasi Perpustakaan Sekolah")
print("================== FORM LOGIN ==================")
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")
input_privilege = input("Masukkan Hak akses/Privilage: ")
print("================================================")

# Memanggil fungsi check_login untuk validasi
login_status, error_form = check_login(input_username, input_password, input_privilege)

# Menampilkan hasil
if login_status:
    print("Login berhasil ..")
    print("Anda Sebagai", input_privilege)
else:
    print("Login gagal.", error_form, "Salah")
    print("Anda Sebagai", input_privilege)