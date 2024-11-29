import math

# Deklarasi Fungsi
def l_persegi(sisi):
    hitung = sisi * sisi
    print(f'Luas persegi adalah {hitung}')

def l_persegi_panjang(p,l):
    hitung = p * l 
    print(f'Luas Persegi Panjang adalah {hitung}')

def l_segitiga(alas, tinggi):
    hitung = 1/2 * alas * tinggi
    print(f'Luas Segitiga adalah {hitung}')

def l_lingkaran(r):
    hitung = r * 3.14 * r
    print(f'Luas Lingkaran adalah {hitung}')

def l_jajargengjang(alas, tinggi):
    hitung = alas * tinggi
    print(f'Luas Jajar Genjang adalah {hitung}')