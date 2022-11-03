umur = int(input("input umur:"))

if umur >=21:
    print("DEWASA")
elif umur >=13:
    print("REMAJA")
elif umur >=9:
    print("BIMBINGAN ORANG TUA")
elif umur <9:
    print("SEMUA USIA")
else:
    print("Invalid Input!")
