#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

#================================================
# Selection sort ascending
#================================================

def selection_sort_asc(data):
    n = len(data)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j
        
        data[i], data[min_index] = data[min_index], data[i]

angka = [20,30,40,90,50,60,70,80,100,110]
selection_sort_asc(angka)
print(angka)