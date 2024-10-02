print("##  Program Python Menghitung Gaji Karyawan  ##")
print("===============================================")
print()

def hitung_upah(golongan):
    if golongan == 'A':
        return 5000
    elif golongan == 'B':
        return 7000
    elif golongan == 'C':
        return 8000
    elif golongan == 'D':
        return 10000
    else:
        print("Golongan tidak valid.")
        exit()

def hitung_uang_lembur(jam_kerja):
    if jam_kerja > 48:
        return (jam_kerja - 48) * 4000
    else:
        return 0

def hitung_gaji(nama, golongan, jam_kerja):
    upah_per_jam = hitung_upah(golongan)
    uang_lembur = hitung_uang_lembur(jam_kerja)
    gaji = (jam_kerja * upah_per_jam) + uang_lembur
    print(f"{nama} menerima upah Rp. {gaji:,} per minggu")

nama = input("Nama Karyawan : ")
golongan = input("Golongan : ").upper()
jam_kerja = int(input("Jumlah jam kerja : "))

print()
hitung_gaji(nama, golongan, jam_kerja)