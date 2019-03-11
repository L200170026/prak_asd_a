##NO.6
##Membuat kelas baru dengan nama Siswa

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

class Siswa(Manusia):
    """Class Siswa yang dibangun dari class Manusia"""
    def __init__(self,nama,Nisn,kelas,alamat):
        self.nama = nama
        self.no = Nisn
        self.kelas = kelas
        self.alamat = alamat
    def __str__(self):
        a = "Nama : "+self.nama+'\n'+"No Induk : "+str(self.no)+'\n'+"Tinggal di : "+self.alamat+'\n'+"Kelas : "+str(self.kelas)
        print (a)
    def ambilNama(self):
        print (self.nama)
    def ambilNisn(self):
        print (self.no)
    def ambilKelas(self):
        print (self.kelas)
    def ambilAlamat(self):
        print (self.alamat)
        
##Eksekusi program 
a = Siswa("Jessica",10345 ,12 ,"Solo")


