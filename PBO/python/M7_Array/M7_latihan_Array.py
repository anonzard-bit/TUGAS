#1. Membuat list angka
angka = [10, 20, 30, 40, 50]
print("List awal:", angka) # Output: List awal: [10, 20, 30, 40, 50]

# 2. Mengakses elemen pertama
print("Elemen pertama:", angka[0]) # Output: Elemen pertama: 10

# 3. Menambah angka 60 ke akhir list
angka.append(60)
print("Setelah ditambah:", angka) # Output: Setelah ditambah: [10, 20, 30, 40, 50, 60]

# 4. Menampilkan semua elemen menggunakan perulangan
print("Menampilkan semua elemen:")
for nilai in angka:
    print(nilai)