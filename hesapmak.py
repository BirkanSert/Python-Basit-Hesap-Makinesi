# Toplama işlemi
def toplam(x, y):
    return x + y

# Çıkarma işlemi
def cikarma(x, y):
    return x - y

# Çarpma işlemi
def carpim(x, y):
    return x * y

# Bölme işlemi
def bolme(x, y):
    if y == 0:
        return "Bir sayi sifira bolunemez."
    else:
        return x / y

print("Yapmak istediginiz islemi secin:")
print("1. Toplama")
print("2. Cikarma")
print("3. Carpma")
print("4. Bolme")

# Kullanıcıdan işlem seçimini alma
secim = input("Seciminiz (1/2/3/4): ")

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == '1':
    print(sayi1, "+", sayi2, "=", toplam(sayi1, sayi2))

elif secim == '2':
    print(sayi1, "-", sayi2, "=", cikarma(sayi1, sayi2))

elif secim == '3':
    print(sayi1, "*", sayi2, "=", carpim(sayi1, sayi2))

elif secim == '4':
    print(sayi1, "/", sayi2, "=", bolme(sayi1, sayi2))

else:
    print("Lütfen Geçerli Bir İşlem Seçiniz")
