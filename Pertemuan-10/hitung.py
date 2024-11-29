import math

def tambah(angka1, angka2):
    hitung = angka1 + angka2
    print(f'Hasil tambah tersebut adalah', angka1, '+', angka2, 'adalah', hitung) 

def kurang(angka1, angka2):
    hitung = angka1 - angka2
    print(f'Hasil kurang tersebut adalah', angka1, '-', angka2, 'adalah', hitung) 

def bagi(angka1, angka2):
    hitung = angka1 / angka2
    print(f'Hasil bagi tersebut adalah', angka1, '/', angka2, 'adalah', hitung) 

def kali(angka1, angka2):
    hitung = angka1 * angka2
    print(f'Hasil kali tersebut adalah', angka1, '*', angka2, 'adalah', hitung) 

def pangkat(angka1, angka2):
    hitung = math.pow(angka1, angka2)
    print(f'Hasil dari {angka1} pangkat {angka2} adalah {hitung}')