#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

#================================================
# Bubble sort descending
#================================================

def bubbleSortDesc(data):
    tukar = True
    batas = len(data) - 1

    while batas > 0 and tukar:
        tukar = False
        for i in range(batas):
            if data[i] < data[i+1]:
                tukar = True
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
        batas = batas - 1

angka = [20,30,40,90,50,60,70,80,100,110]
bubbleSortDesc(angka)
print(angka)