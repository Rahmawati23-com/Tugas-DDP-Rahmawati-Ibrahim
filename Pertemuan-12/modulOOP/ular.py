from animal import animal

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, kulit, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.kulit = kulit
        self.habitat = habitat

    def info_ular(self):
        super().info_animal(),
        print("kulit \t\t\t :", self.kulit, 
              "\nhabitat \t\t :", self.habitat)
        
ular_cobra = ular("cobra", "reptil", "darat", "bertelur", "berbisa", "hutan")
ular_cobra.info_ular()