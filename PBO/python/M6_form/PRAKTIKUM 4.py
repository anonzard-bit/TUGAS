# Program Menghitung Harga Setelah Diskon
import datetime as gendeng
# Input data
store_name = input("Nama Toko: ")
purchase_date = gendeng.datetime.today()
cashier_name = input("Nama Kasir: ")
customer_name = input("Nama Pelanggan: ")
total_purchase = float(input("Total Pembelian: Rp "))

# Proses diskon
if total_purchase > 300000:
    discount = 0.3 * total_purchase
elif total_purchase > 100000:
    discount = 0.15 * total_purchase
elif total_purchase > 50000:
    discount = 0.02 * total_purchase
else:
    discount = 0

# Hitung harga akhir
final_price = total_purchase - discount

# Output hasil
print("\n--- STRUK PEMBELIAN ---")
print("Nama Toko       :", store_name)
print("Tanggal         :", purchase_date)
print("Nama Kasir      :", cashier_name)
print("Nama Pelanggan  :", customer_name)
print("Total Pembelian : Rp", total_purchase)
print("Diskon          : Rp", discount)
print("Harga Akhir     : Rp", final_price)
