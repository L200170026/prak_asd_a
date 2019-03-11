class Pesan(object):
    """Sebuah class bernama Pesan.
    Untuk memahami konsep Class dan Object"""
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai', len(self.teks), 'karaktaer.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, kata):
        self.kata = kata
        if self.kata in self.teks:
            return True
        else:
            return False
    def hitungKonsonan(self):
            x = self.teks
            vkl = 'aiueoAIUEO'
            jml = 0
            for i in x :
                if i.lower() not in vkl :
                    jml += 1
            return jml
    def hitungVokal(self):
            y = self.teks
            vkl = 'AIUEOaiueo'
            jml = 0
            for j in y :
                if j in vkl:
                    jml += 1
            return jml
        
