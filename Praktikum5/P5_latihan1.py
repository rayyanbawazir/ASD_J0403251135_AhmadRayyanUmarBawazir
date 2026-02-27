#================================================
# Nama : Ahmad Rayyan Umar Bawazir
# NIM : J0403251135
# Kelas : TPL A2
#================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    # Fungsi pangkat menerima dua parameter:
    # a = bilangan pokok (misalnya 2)
    # n = eksponen (misalnya 4)

    # Base case
    # Jika n sama dengan 0, maka hasilnya adalah 1
    # sesuai aturan matematika: a^0 = 1
    if n == 0:
        return 1

    # Recursive case (pemanggilan fungsi itu sendiri)
    # Fungsi memanggil dirinya dengan nilai n-1
    # lalu hasilnya dikalikan dengan a
    return a * pangkat(a, n - 1)

# Memanggil fungsi pangkat dengan a = 2 dan n = 4
# Artinya menghitung 2^4
print(pangkat(2, 4))

# Output yang dihasilkan adalah: 16

"""
 Program ini menghitung pangkat dengan cara memanggil fungsi secara 
 berulang sampai nilai n menjadi 0. Setelah itu, hasil perkalian dikembalikan 
 satu per satu hingga diperoleh hasil akhir, yaitu 2^4 = 16
"""