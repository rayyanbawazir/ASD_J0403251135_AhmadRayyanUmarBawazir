#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

#================================================
# Shell sort descending
#================================================

def shell_sort_desc(data):
    gap = len(data) // 2
    
    while gap > 0:
        for i in range(gap, len(data)):
            temp = data[i]
            j = i
            
            while j >= gap and data[j-gap] < temp:
                data[j] = data[j-gap]
                j -= gap
            
            data[j] = temp
        gap //= 2

angka = [20,30,40,90,50,60,70,80,100,110]
shell_sort_desc(angka)
print(angka)