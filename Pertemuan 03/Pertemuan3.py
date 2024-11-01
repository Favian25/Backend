#Function
def sapa_lisa():
    print("Hai Lisa")

sapa_lisa()

#Function dengan parameter
def hitung_luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga : ", luas)

hitung_luas_segitiga(4, 8)

#Return dalam function
def harga_setelah_pajak(harga_dasar):
    return harga_dasar + (harga_dasar * 10/100)

harga_bakso = 10000
total_harga = harga_setelah_pajak(harga_bakso)
print("Harga bakso 1 porsi Rp.", total_harga)

#Default Parameter
def tambah(var1 = 5, var2 = 2):
    return var1 + var2

print(tambah())
print(tambah(1))
print(tambah(1, 2))
print(tambah(5, 4))

def pangkat(angka, pangkat = 2):
    hasil = 1
    for i in range(0, pangkat):
        hasil = hasil * angka
        return hasil

print(pangkat(3))
print(pangkat(7))
print(pangkat(11))

#Args dalam python
def sapa_teman(*args):
    print(args)
    print(type(args))

sapa_teman("Alex", "Lisa", "Sari", "Risa")

#Kwargs dalam Python
def sambung_kata(**kwargs):
    print(kwargs)
    print(type(kwargs))

sambung_kata(a= "Belajar", b= "Python", c= "di", d= "STIKOM")