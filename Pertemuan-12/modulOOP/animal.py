class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang = berkembang_biak

    def makan(self):
        print(f"{self.nama} sedang makan {self.makanan}")

    def info_animal(self):
        print("nama \t\t\t: ", self.nama,
              "\nMakanan \t\t: ", self.makanan,
              "\nHidup \t\t\t: ", self.hidup,
              "\nberkembangbiak \t\t: ", self.hidup,
              )

binatang = animal("kambing", "rumput", "10 tahun", "melahirkan")
binatang.makan()
binatang.info_animal()
    