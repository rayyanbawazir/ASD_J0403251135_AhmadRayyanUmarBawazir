#buka file dalam satu string
print("----Membuka File Dalam Satu String----")
with open("datamahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("tipe data: ", type(isi_file))
print(" ")


#buka file per baris
print("----Membuka File Per Baris String----")
jumlah_baris = 0
with open("datamahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print("isinya : ", baris)
print(" ")
        
        
#parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data
print("----parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data----")

with open("datamahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter garis baru
        nim, nama, nilai = baris.split(",")
        print("NIM:", nim, "|Nama:", nama, "|Nilai:", nilai)
        
# ======================================================================

data_list = [] #inisialisasi list untuk menampung data

with open("datamahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter garis baru
        nim, nama, nilai = baris.split() #pecah menjadi data satuan dan simpan ke variabel
        data_list.append([nim, nama, int(nilai)]) #menyimpan data ke list
print("==== Menampilkan LIst ====")
print(data_list)
print("Contoh record ke-1", data_list[0])
print("Contoh record ke-1", data_list[2])
print("Jumlah record adalah", len(data_list))

#=============================================================================
# Praktikum 1: konsep ADT dan file handling
# Latihan dasar 4 membaca dan menyimpan ke struktur data dictinonary
#=============================================================================

print(" ")

data_dict = {}

with open("datamahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter garis baru
        nim, nama, nilai = baris.split() #pecah menjadi data satuan dan simpan ke variabel
        #simpan data dalam dictionary
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("==== Menampilkan Data Dictionary ====")
print(data_dict)


        
