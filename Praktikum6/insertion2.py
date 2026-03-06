#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

#================================================
# Insertion sort descending
#================================================

def insertion_sort_desc(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        while j >= 0 and data[j] < key:
            data[j+1] = data[j]
            j = j - 1
        
        data[j+1] = key

angka = [20,30,40,90,50,60,70,80,100,110]
insertion_sort_desc(angka)
print(angka)