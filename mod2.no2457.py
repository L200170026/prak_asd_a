##Modul 2. jawaban NO 2abc, 4, 5, 7
##JESSICA / L200170026

class Manusia(object):
    """class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n * 2
    
class Mahasiswa(Manusia):
    """Class Mahasiswa yang di bangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ',NIM ' + str(self.NIM)\
            + '. Tinggal di ' + self.kotaTinggal\
            + '. Uang saku Rp ' + str(self.uangSaku)\
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = 'kenyang'
##NO 2
##(a) Metode untuk mengambil kota tempat tinggal mahasiswa
    def ambilKotaTinggal(self):
        return self.kotaTinggal
##(b) Metode untuk memperbarui kota tinggal
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal = ubah
##(c) Metode untuk menambah uang saku
    def tambahUangSaku(self, tambah):
        self.uangSaku += tambah

##NO 3 di file sendiri

##NO 4
    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
##NO 5
    def hapusKuliah(self, item):
        self.listKuliah.remove(item)

##NO 6 di file sendiri
        
##NO 7
class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanpy(self):
        print('Python is cool.')
##Class Manusia:
##    1. nama
##    2. keadaan
##    3. ucapkanSalam
##    4. makan
##    5. olahraga
##    6. mengalikanDenganDua
##
##Class Mahasiswa:
##    1. NIM
##    2. kotaTinggal
##    3. uangsaku
##    4. ambilNama
##    5. ambilNIM
##    6. ambilUangSaku
##    7. makan
##    8. ambilKotaTinggal
##    9. perbaruiKotaTinggal
##    10. tambahUangSaku
##    11. listKuliah
##    12. ambilKuliah
##    13. hapusKuliah
##
##Class MhsTIF:
##    1. katakanpy
