import math

def l_balok(p, l, t):
    hitung = 2 * (p*l)+(p*t)+(l*t)
    print(f'Luas Balok adalah {hitung}')

def l_kubus(sisi):
    hitung = 6 * math.pow(sisi, 2)
    print(f'Luas Kubus adalah {hitung}')

def l_tabung(r, t):
    hitung = 2 * 3.14 * r * (r+t)
    print(f'Luas permukaan tabung adalah {hitung}')

def l_limassegitiga(a, t):
    hitung = 1/2 * a * t
    print(f'luas limas segitiga adalah {hitung}')

def l_prismasegitiga(a, t, P):
    luas_alas = 1/2 * a * t
    keliling_alas = 3 * a 
    luas_sisi_tegak = P * keliling_alas
    luas_total = 2 * luas_alas + luas_sisi_tegak
    print(f'Luas permukaan prisma segitiga adalah {luas_total:.2f} satuan luas.')

