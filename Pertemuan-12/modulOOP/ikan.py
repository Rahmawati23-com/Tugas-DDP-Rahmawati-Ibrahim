from animal import animal

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, jenis):
        super ().__init__(nama, makanan, hidup, berkembang_biak),
        self.warna = warna
        self.jenis = jenis

    def info_ikan(self):
        super().info_animal(),
        print("warna \t\t\t :", self.warna, 
              "\njenis \t\t\t :", self.jenis)
        
ikan_nemo = ikan("nemo", "alga", "air", "bertelur", "biru", "ikan hias")
ikan_nemo.info_ikan()