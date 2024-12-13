class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def berjalan(self):
        print(f"{self.name} sedang berjalan")

    def ngomong(self):
        if self.name == 'pria':
            print(f"{self.name} tidak bercerita karena dia {self.gender}")
        else:
            print(f"{self.name} senang bercerita karena dia {self.gender}")

class supir(person):
    def __init__(self, name, age, gender, sim):
        super().__init__(name, age, gender)
        self.sim = sim 
    
    def berkendara(self):
        print(f"{self.name} sedang berkendara dengan SIM {self.sim}")

class mahasiswa(person):
    def __init__(self, name, age, gender, nim):
        super().__init__(name, age, gender)
        self.nim = nim

    def belajar(self):
        print(f"{self.name} mahasiswa tersebut sedang belajar")

budi = person('budi', 20, 'pria')
budi.ngomong()

sri = mahasiswa('sri', 18, 'perempuan', '0110124136')
sri.berjalan()
sri.belajar()