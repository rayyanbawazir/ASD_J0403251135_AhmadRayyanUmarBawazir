#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

#================================================
# Selection sort descending
#================================================

def selection_sort_desc(data):
    n = len(data)
    
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if data[j] > data[max_index]:
                max_index = j
        
        data[i], data[max_index] = data[max_index], data[i]

angka = [20,30,40,90,50,60,70,80,100,110]
selection_sort_desc(angka)
print(angka)