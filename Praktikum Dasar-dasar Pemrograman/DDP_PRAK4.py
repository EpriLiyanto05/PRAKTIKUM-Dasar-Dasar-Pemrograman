﻿# DDP LAB-4
# Nama: Epri Liyanto
# NIM: 0110120113

# SOAL 1 - Mencetak nama
# Tuliskan program untuk Soal 1 di bawah ini

#Masukkan nama anda 
x = input("Masukkan nama: ")
#menghitung jumlah kata dengan len
jumlah = len(x)
i = 0
while i < jumlah:
  i = i + 1
#mengeprint nama dengan string slicing, maka akan terbentuk perkata setiap perulangan
  print(x[0:i])
print()
    

# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini

while True:
#masukkanlah sebuah teks
  teks = input("Masukkan sebuah teks: ")
#hitung teks dengan len
  jumlahhuruf = len(teks)
#Teks valid jika huruf lebih dari 8
  if (jumlahhuruf >= 8 
#dan teks harus diawali dengan NF, nf, Nf, atau nF pilih salah satu
  and (teks.startswith("NF") or teks.startswith("Nf") or teks.startswith("nF") or teks.startswith("nf"))
# Tekspun harus diakhiri dengan YYY atau yyy
  and (teks.endswith("YYY") or teks.endswith("yyy")) 
#Juga harus mengandung angka 0-9
  and not (teks.isalpha())):
#Jika sudah sesuai dengan klasifikasi maka teks yang dimasukkan valid dan program berhenti
    print("Teks valid, program berhenti")
    break
#Jika tidak maka teks tidak valid dan program akan mengulang untuk memasukkan teks 
  else:
    print("Teks tidak valid")
