class orang:
    #variabel (property)
    def __init__(self, nama, usia, gender, alamat):
        self.nama = nama
        self.usia = usia 
        self.gender = gender
        self.alamat = alamat

    def ngomong(self):
        print("saya bisa berbicara karena saya, ", self.nama)

    def jalan (self, kata):
        print("saya mau jalan, ", kata)