totalBarang = int(input("Total barang: "))
totalHarga = 0

for i in range(1, totalBarang + 1):
    hargaBarang = int(input(f"Masukan harga barang {i}: "))
    totalHarga += hargaBarang

print("Total harga semua barang:", totalHarga)