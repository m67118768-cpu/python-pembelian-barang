print("PEMBELIAN BARANG")

barang = input("Nama barang: ")
harga = int(input("Harga barang: "))
jumlah = int(input("Jumlah beli: "))

total = harga * jumlah

if total >= 100000:
    diskon = total * 25 / 100
else:
    diskon = 0

bayar = total - diskon

print("Nama barang:", barang)
print("Total harga:", total)
print("Diskon:", int(diskon))
print("Total bayar:", int(bayar))
