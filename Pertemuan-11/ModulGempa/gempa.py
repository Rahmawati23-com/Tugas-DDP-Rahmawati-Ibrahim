class Gempa:
    lokasi = ' '
    skala = ' '

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            ket = 'Gempa tidak berasa'
        elif 2 <= self.skala < 4:
            ket = 'bangunan retak retak'
        elif 4 <= self.skala < 6:
            ket = 'bangunan roboh'
        else:
            ket = 'Bangunan roboh dan berpotensi tsunami'

        print('Lokasi Gempa', self.lokasi, '\nSkala Gempa', self.skala, '\nDampak Gempa', ket)
        print('_____'*5)



