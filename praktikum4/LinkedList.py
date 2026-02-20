#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

#================================================
# Implementasi dasar : node pada linked list
#================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
        
#1. membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2. membuat node A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#4. Traversal : Menelusuri node dari head sampai ke none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya
    


