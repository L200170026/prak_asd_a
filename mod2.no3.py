##NO 3 membuat program memasukkan data lewat Python Shell
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
        
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal = ubah
    def tambahUangSaku(self, tambah):
        self.uangSaku += tambah

##NO 3
print("Silahkan Masukkan Data Mahasiswa Di bawah Ini :")
a = input("Nama Mahasiswa      : ")
b = input("NIM Mahasiswa       : ")
c = input("Asal Mahasiswa      : ")
d = input("Uang Saku Mahasiswa : ")
mhs = Mahasiswa(a, b, c, d)
print("""Silahkan Ketik 'mhs.instruksi' untuk menjalankan program yang
diinginkan.""")
