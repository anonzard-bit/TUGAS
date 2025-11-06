print("Program memasukkan Nilai ke dalam Array")
print("---------------------------------------")
print("By: Rayya, Filbian, Reza, Zakky")
print("---------------------------------------")

n = int(input("Masukkan jumlah elemen Array: "))

nilai = []

for i in range(n):
    data = int(input(f"Nilai ke-{i+1}: "))
    nilai.append(data)

rata_rata = sum(nilai)/n
print(f"Rata-rata nilai: {rata_rata:.2f}")