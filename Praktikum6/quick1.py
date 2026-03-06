#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

#================================================
# Quick sort ascending
#================================================

def quick_sort_asc(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        kecil = [x for x in data[1:] if x <= pivot]
        besar = [x for x in data[1:] if x > pivot]
        return quick_sort_asc(kecil) + [pivot] + quick_sort_asc(besar)

angka = [20,30,40,90,50,60,70,80,100,110]
hasil = quick_sort_asc(angka)
print(hasil)