#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum dengan Rekursi
# ==========================================================

def cari_maks(data, index=0):
    # Base case: jika index sudah di elemen terakhir list
    # maka kembalikan nilai elemen tersebut
    if index == len(data) - 1:
        return data[index]

    # Recursive case: cari nilai maksimum dari sisa list (index berikutnya)
    maks_sisa = cari_maks(data, index + 1)

    # Bandingkan elemen sekarang dengan hasil maksimum dari sisa list
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

# List angka yang akan dicari nilai maksimumnya
angka = [3, 7, 2, 9, 5]

# Menampilkan hasil nilai maksimum
print("Nilai maksimum:", cari_maks(angka))

"""
Program ini mencari angka terbesar dengan memeriksa data satu per satu secara rekursif. 
Saat sampai di elemen terakhir (base case), nilainya dikembalikan. Sebelumnya, 
fungsi terus memanggil dirinya sendiri (recursive call) dan membandingkan angka hingga
diperoleh nilai paling besar.
"""