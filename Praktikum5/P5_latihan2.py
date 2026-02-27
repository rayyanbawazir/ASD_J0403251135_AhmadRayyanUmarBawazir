#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================
def countdown(n):
    # Jika n sama dengan 0, maka program berhenti
    if n == 0:
        print("Selesai")
        return   # Menghentikan fungsi agar tidak lanjut lagi

    # Menampilkan nilai n saat fungsi pertama kali masuk
    print("Masuk:", n)

    # Fungsi memanggil dirinya sendiri dengan nilai n-1 
    countdown(n - 1)

    # Menampilkan nilai n saat fungsi selesai dijalankan 
    print("Keluar:", n)

# Memanggil fungsi countdown dengan nilai awal 3
countdown(3)

"""
    Output “Keluar” muncul terbalik karena fungsi rekursi berjalan seperti tumpukan.
    Program masuk terus sampai n = 0, lalu baru kembali satu per satu dari pemanggilan terakhir.
    Karena yang dipanggil terakhir selesai lebih dulu, maka yang dicetak dulu adalah Keluar: 1, 
    lalu Keluar: 2, dan terakhir Keluar: 3.
"""