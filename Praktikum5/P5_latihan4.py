#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf dengan Rekursi
# ==========================================================

def kombinasi(n, hasil=""):
    # Fungsi kombinasi menerima:
    # n = panjang kombinasi huruf yang ingin dibuat
    # hasil = string sementara untuk menyimpan kombinasi huruf

    # Base case:
    # Jika panjang string hasil sudah sama dengan n,
    # maka cetak hasil dan hentikan fungsi
    if len(hasil) == n:
        print(hasil)
        return

    # Recursive call 1:
    # Memanggil fungsi kembali dengan menambahkan huruf "A"
    kombinasi(n, hasil + "A")

    # Recursive call 2:
    # Memanggil fungsi kembali dengan menambahkan huruf "B"
    kombinasi(n, hasil + "B")

# Memanggil fungsi kombinasi dengan panjang huruf = 2
kombinasi(2)


"""
Jumlah kombinasi bertambah karena di setiap posisi huruf selalu ada dua pilihan,
yaitu A dan B. Jadi untuk setiap tambahan panjang satu huruf, jumlah kombinasi menjadi 
dua kali lipat. Misalnya saat n = 2 ada 4 kombinasi, dan saat n = 3 ada 8 kombinasi.    
"""