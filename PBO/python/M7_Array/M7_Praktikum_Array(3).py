# Program Memasukkan Nilai ke dalam Array

print("Program Memasukkan Nilai ke dalam Array")
print(20*"=")
print("By : Rayya, Filbian, Reza, Zakky")
print(20*"=")

# 1. Input jumlah elemen
jumlah_elemen = int(input("Masukkan jumlah elemen Array: "))

# 2. Inisialisasi variabel
daftar_nilai = []
total_nilai = 0

# 3. Input nilai ke dalam array
print("-" * 30)
for i in range(1, jumlah_elemen + 1):
    nilai = float(input("Nilai ke-" + str(i) + ": "))
    daftar_nilai.append(nilai)
    total_nilai = total_nilai + nilai  # menjumlahkan nilai

# 4. Hitung rata-rata
rata_rata = total_nilai / jumlah_elemen

# 5. Tampilkan hasil
print("-" * 30)
print("Rata-rata Nilai:", rata_rata)