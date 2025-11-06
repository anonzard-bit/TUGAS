# print
print("Program memasukkan Nilai ke dalam Array")
print("---------------------------------------")
print("By: Rayya, Filbian, Reza, Zakky")
print("---------------------------------------")

# Input
n = int(input("Masukkan jumlah elemen Array: "))

# proses
nilai = []

# masukkan nilai kedalam array
for i in range(n):
    data = float(input(f"Nilai ke-{i+1}: "))
    nilai.append(data)

# menghitung rata-rata
rata_rata = sum(nilai)/n
print(f"Rata-rata nilai: {rata_rata:.1f}")