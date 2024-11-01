angka_pilihan = int(input("""masukkan pilihan
                          :
                          1. menghitung luas persegi
                          2. menghitung luas lingkaran
                          3. menghitung luas segitiga 
                          """))

match angka_pilihan:
    case 1:
        print("menghitung luas persegi")
        sisi = int(input("Masukkan panjang sisi persegi: "))
        luas_persegi = sisi ** 2
        print(f"Luas Persegi adalah: {luas_persegi}")

    case 2:
        radius = int(input("Masukkan jari-jari lingkaran: "))
        luas_lingkaran = phi * radius ** 2
        print(f"Luas Lingkaran adalah: {luas_lingkaran}")

    case 3:
        alas = int(input("Masukkan panjang alas segitiga: "))
        tinggi = int(input("Masukkan tinggi segitiga: "))
        luas_segitiga = 0.5 * alas * tinggi
        print(f"Luas Segitiga adalah: {luas_segitiga}")
    
    case _:
        print("Salah pilih. Pilihan tidak tersedia.")