import os

# Aplikasi Manajemen Data Siswa
siswa_list = []

while True:
    os.system('cls')  # Untuk Windows, gunakan 'clear' jika di Linux/Mac
    print("\n=== APLIKASI MANAJEMEN DATA SISWA ===")
    print("1. Tambah Data Siswa")
    print("2. Lihat Data Siswa")
    print("3. Update Data Siswa")
    print("4. Hapus Data Siswa")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        os.system('cls')
        print("\n=== Tambah Data Siswa ===")
        nama = input("Nama: ")
        nis = input("NIS: ")
        kelas = input("Kelas: ")
        alamat = input("Alamat: ")
        siswa = [nis, nama, kelas, alamat]
        siswa_list.append(siswa)
        print("   Data siswa berhasil ditambahkan!")
        input("\n(Klik apapun untuk melanjutkan!)")

    elif pilihan == "2":
        os.system('cls')
        print("\n=== Daftar Data Siswa ===")
        if not siswa_list:
            print("Belum ada data siswa.")
        else:
            for no, siswa in enumerate(siswa_list, start=1):
                print(f"{no}. NIS: {siswa[0]}, Nama: {siswa[1]}, Kelas: {siswa[2]}, Alamat: {siswa[3]}")
        input("\n(Klik apapun untuk melanjutkan!)")

    elif pilihan == "3":
        os.system('cls')
        print("\n=== Update Data Siswa ===")
        if not siswa_list:
            print("Belum ada data siswa.")
        else:
            for no, siswa in enumerate(siswa_list, start=1):
                print(f"{no}. NIS: {siswa[0]}, Nama: {siswa[1]}, Kelas: {siswa[2]}, Alamat: {siswa[3]}")
            try:
                index = int(input("Masukkan nomor siswa yang ingin diupdate: ")) - 1
                if 0 <= index < len(siswa_list):
                    print("Kosongkan jika tidak ingin mengubah data.")
                    nama = input(f"Nama ({siswa_list[index][1]}): ")
                    nis = input(f"NIS ({siswa_list[index][0]}): ")
                    kelas = input(f"Kelas ({siswa_list[index][2]}): ")
                    alamat = input(f"Alamat ({siswa_list[index][3]}): ")

                    if nama: siswa_list[index][1] = nama
                    if nis: siswa_list[index][0] = nis
                    if kelas: siswa_list[index][2] = kelas
                    if alamat: siswa_list[index][3] = alamat

                    print("   Data siswa berhasil diperbarui!")
                else:
                    print("  Nomor tidak valid!")
            except ValueError:
                print("  Input harus berupa angka!")
        input("\n(Klik apapun untuk melanjutkan!)")

    elif pilihan == "4":
        os.system('cls')
        print("\n=== Hapus Data Siswa ===")
        if not siswa_list:
            print("Belum ada data siswa.")
        else:
            for no, siswa in enumerate(siswa_list, start=1):
                print(f"{no}. NIS: {siswa[0]}, Nama: {siswa[1]}, Kelas: {siswa[2]}, Alamat: {siswa[3]}")
            try:
                index = int(input("Masukkan nomor siswa yang ingin dihapus: ")) - 1
                if 0 <= index < len(siswa_list):
                    hapus = siswa_list.pop(index)
                    print(f"   Data siswa '{hapus[1]}' berhasil dihapus!")
                else:
                    print("  Nomor tidak valid!")
            except ValueError:
                print("  Input harus berupa angka!")
        input("\n(Klik apapun untuk melanjutkan!)")

    elif pilihan == "5":
        print("          Terima kasih telah menggunakan aplikasi ini.")
        break

    else:
        print("  Pilihan tidak valid! Silakan pilih 1-5.")
        input("\n(Klik apapun untuk melanjutkan!)")
