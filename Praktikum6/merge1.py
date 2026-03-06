#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

#================================================
# Merge sort ascending
#================================================

def merge_sort_asc(data):
    if len(data) > 1:
        mid = len(data) // 2
        kiri = data[:mid]
        kanan = data[mid:]

        merge_sort_asc(kiri)
        merge_sort_asc(kanan)

        i = j = k = 0

        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                data[k] = kiri[i]
                i += 1
            else:
                data[k] = kanan[j]
                j += 1
            k += 1

        while i < len(kiri):
            data[k] = kiri[i]
            i += 1
            k += 1

        while j < len(kanan):
            data[k] = kanan[j]
            j += 1
            k += 1

angka = [20,30,40,90,50,60,70,80,100,110]
merge_sort_asc(angka)
print(angka)