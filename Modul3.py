##JESSICA GUSTIN RAHAJENG
##L200170026/A

m1 = [[5,8],[9,6]]
m2 = [[15,23],[9,7]]
#NO 1A
def cekMatriks(mtrx):
    """Memastikan type data Integer"""
    jum = len(mtrx)
    hasil = ""
    for x in mtrx:
        for i in x:
            assert isinstance(i, int),"Harus Integer"
        return True
#NO 1B
def Ukuran(mtrx):
    """Mengambil ukuran matriks"""
    return("Ukuran Matriks = "+str(len(mtrx))+" x "+str(len(mtrx[0])))
#NO 1C
def Jumlah(mtrx1,mtrx2):
    """Penjumlahan 2 Matriks"""
    if Ukuran(mtrx1) == Ukuran(mtrx2):
        for x in range(0, len(mtrx1)):
            for y in range(0, len(mtrx1[0])):
                print(mtrx1[x][y] + mtrx2[x][y], end=' '),
            print()
    else:
        print("Matriks Tidak Sesuai")
#NO 1D
def Kali(mtrx1,mtrx2):
    """Perkalian 2 Matriks"""
    mat3 = []
    if Ukuran(mtrx1) == Ukuran(mtrx2):
        for x in range(0, len(mtrx1)):
            row = []
            for y in range(0, len(mtrx1[0])):
                total = 0
                for z in range(0, len(mtrx1)):
                    total = total + (mtrx1[x][z] * mtrx2[z][y])
                row.append(total)
            mat3.append(row)

        for x in range(0, len(mat3)):
            for y in range(0, len(mat3[0])):
                print(mat3[x][y], end=' ')
            print()
    else:
        print("Matriks Tidak Sesuai")
def determinan(mtrx):
    """Menghitung Determinan Matriks"""
    if len(mtrx) == len(mtrx[0]):
        bil = [x for x in range(len(mtrx))]
        jum = 0
        for i in range(len(mtrx)):
            total = 1
            for x in range(len(mtrx)):
                total *= mtrx[x][bil[x]]
            bil += [bil.pop(0)]
            jum += total
        bil2 = [x for x in range(len(mtrx))]
        bil.reverse()
        jum2 = 0
        for i in range(len(mtrx)):
            total2 = 1
            for x in range(len(mtrx)):
                total2 *= mtrx[x][bil2[x]]
            bil2 += [bil2.pop()]
            jum2 += total2
        print(total-total2)
        return ""
    else:
        print("Matriks Harus Bujursangkar")

#CEK NO 1
print(cekMatriks(m1))
print(Ukuran(m1))
Jumlah(m1,m2)
Kali(m1,m2)
print(determinan(m1))

#NO 2A
def buatNol(n,m=None):
    if(m==None):
        m=n
    print("Membuat matriks 0 dengan ordo "+str(n)+"x"+str(m))
    print([[0 for j in range(m)] for i in range(n)])

buatNol(2,4)
buatNol(3)

def buatIdentitas(n):
    print("Membuat matriks identitas dengan ordo"+str(n)+"x"+str(n))
    print([[1 if j==i else 0 for j in range(n)] for i in range(n)])

buatIdentitas(4)
buatIdentitas(2)

#NO 3
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
    def pushAwal(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    def pushAkhir(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    def insert(self,data,pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif pos==0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
                prev = current
                current = current.next
                current_pos +=1
            prev.next = node
            node.next = current
        return self.head
    def deleteNode(self, position): 
        if self.head == None: 
            return 
        temp = self.head 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        next = temp.next.next
        temp.next = None
        temp.next = next 
    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next   
    
llist = LinkedList() 
llist.pushAwal(21)
llist.pushAwal(22)
llist.pushAwal(12)
llist.pushAwal(14)
llist.pushAwal(2)
llist.pushAwal(19)
llist.pushAkhir(9)
llist.deleteNode(0)
llist.insert(1,6)
print(llist.search(21))
print(llist.search(29))
llist.display()

#NO 4
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.prev = None
class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
    def awal(self, new_data):
        print("menambah pada awal", new_data)
        new_node = Node(new_data) 
        new_node.next = self.head 
        if self.head is not None: 
            self.head.prev = new_node 
        self.head = new_node 
    def akhir(self, new_data):
        print("menambah pada akhir", new_data)
        new_node = Node(new_data) 
        new_node.next = None
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
        last = self.head 
        while(last.next is not None): 
            last = last.next
        last.next = new_node 
        new_node.prev = last 
        return
    def printList(self, node): 
        print("\nDari Depan :")
        while(node is not None): 
            print(" % d" %(node.data))
            last = node 
            node = node.next
        print("\nDari Belakang :")
        while(last is not None): 
            print(" % d" %(last.data)) 
            last = last.prev 
llist = DoublyLinkedList() 
llist.awal(7)  
llist.awal(1)
llist.akhir(6)
llist.akhir(4) 
llist.printList(llist.head) 
