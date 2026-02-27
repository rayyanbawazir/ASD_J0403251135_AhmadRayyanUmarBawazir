# ==========================================================
# Studi Kasus: Generator PIN dengan Rekursi
# ==========================================================

def buat_pin(panjang, hasil=""):
    # Fungsi buat_pin menerima:
    # panjang = jumlah digit PIN yang ingin dibuat
    # hasil = string sementara untuk menyimpan PIN yang sedang dibentuk

    # Base case:
    # Jika panjang hasil sudah sama dengan panjang yang diminta
    # maka cetak PIN dan hentikan fungsi
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Loop untuk memilih setiap angka yang bisa digunakan dalam PIN
    for angka in ["0", "1", "2"]:
        # Recursive call:
        # Memanggil fungsi kembali dengan menambahkan satu angka
        # ke variabel hasil
        buat_pin(panjang, hasil + angka)

# Memanggil fungsi buat_pin dengan panjang PIN = 3
buat_pin(3)

"""
 Supaya angka tidak muncul dua kali dalam satu PIN, 
 caranya dengan mengecek dulu apakah angka itu sudah dipakai.
 Kalau sudah ada di hasil, angka tersebut tidak dipilih lagi. 
 Dengan begitu, setiap PIN yang dibuat isinya selalu berbeda.   
"""