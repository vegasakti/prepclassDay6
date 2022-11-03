tahun = int(input("masukan tahun:"))
modulus = tahun % 4
if modulus == 0:
    print("Kabisat")
else:
    print("bukan kabisat")