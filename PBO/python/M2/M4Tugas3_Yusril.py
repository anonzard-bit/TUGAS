# Program input nama, mapel, dan nilai
nama = input("Masukkan nama: ")
mapel = input("Masukkan nama mapel: ")
nilai = float(input("Masukkan nilai: "))
data = [10, 20, 30, 40, 50]
rata_rata = sum(data) / len(data)


print("\n--- Data Nilai ---")
print("Nama     :", nama)
print("Mapel    :", mapel)
print("Nilai    :", nilai)
print("Rata-rata:", rata_rata)

print("\n" , 20*"=", "\n")

# Menghitung Rata" Nilai

nama = input("Masukkan Nama :")
mapel = input("Maskkan Mata Pelajaran :")
nilaiUh = int(input("Masukkan Nilai UH :"))
nilaiUts = int(input("Masukkan Nilai UTS :"))
nilaiUas = int(input("Masukkan Nilai UAS :"))
rata_rata = (nilaiUh + nilaiUts + nilaiUas)/ 3

print("Output :")
print("Nama Siswa :", nama)
print("Mata Pelajaran :", mapel)
print("Nilai UH :", nilaiUh)
print("Nama UTS :", nilaiUts)
print("Nilai UAS :", nilaiUas)
print("Nilai Rata-Rata Adalah :", rata_rata)