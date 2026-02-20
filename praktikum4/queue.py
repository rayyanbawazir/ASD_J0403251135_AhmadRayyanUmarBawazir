#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

#================================================
# Implementasi dasar : Queue
#================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        nodeBaru = Node(data)
        
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
        else:
            self.rear.next = nodeBaru
            self.rear = nodeBaru
    
    def dequeue(self):
        if self.is_empty():
            print("Queue kosong")
            return None
        
        data_terhapus = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        return data_terhapus
                
    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# instansiasi class queue
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
