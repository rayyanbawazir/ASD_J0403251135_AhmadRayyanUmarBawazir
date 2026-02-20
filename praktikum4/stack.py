#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

#================================================
# Implementasi dasar : Stack
#================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
        
#Stack ada operasi push(memasukkan head baru) dan pop (menghapus head)

class stack:
    def __init__(self):
        self.top = None #top menuju ke node paling atas (awalnta kosong)
        
    def is_empty(self):
        return self.top is None
         
    def push(self,data): #memasukkan data baru pada stack
        #1 membuat node baru
        nodeBaru = Node(data) #memanggil konstruktor pada class node
        
        #2 node baru menunjukkan ke top yang lama (head lama)
        nodeBaru.next = self.top
        
        #3 geser top/head pindah ke node baru
        self.top = nodeBaru
        
    def pop(self): #mengambil atau menghapus node paling atas (top/head)
        
        if self.is_empty():
            print("Stack Kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        self.top = self.top.next
        return data_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        
        
        
    def tampilkan(self):
        current = self.top
        print("Top ", end="-> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
#Instatiasi Class Stack 
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top):", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top):", s.peek())


        