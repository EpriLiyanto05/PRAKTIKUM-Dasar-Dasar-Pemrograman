def cetak_nama(nama=''):
  # Tulis kode fungsi cetak_nama di bawah ini
  # Hapus pass jika implementasi sudah dibuat

  #jika tidak ada nama yg dimasukkan maka program mencetak 'tidak ada nam yang dimasukkan'
  if nama == '':
    print('Tidak ada nama yang dicetak')
  else:
  #di sini huruf dihitung panjangnya
    jumlahhuruf = len(nama)
    i = 0
  #program mengulang huruf 
    while i < jumlahhuruf:
      i = i + 1
  #jika i sudah sama jumlahnya dengan nama maka akan ditambah karakter '!'
      if (i == jumlahhuruf):
         print(nama[0:i] + '!')
  #dan jika belum sama maka karakter '!' tidak dicetak
      else:
         print(nama[0:i])


def hitung_kesamaan(kata1, kata2):
  # Tulis kode fungsi hitung_kesamaan di bawah ini
  # Hapus pass jika implementasi sudah dibuat

  #di sini akan dihitung terbesar panjangnya huruf
  terbesar = max(len(kata1), len(kata2))

  hurufsama = 0
  for i in range(terbesar):
  #membandingkan antara kata1 dengan kata2
    if (kata1[i:i+1] == kata2[i:i+1]):
      hurufsama = hurufsama + 1
  #jika ada huruf yang sama maka dicetak jumlah huruf yang sama tersebut
  print('jumlah huruf sama', hurufsama)


def hitung(bil1, bil2, operator='+'):
  # Tulis kode fungsi hitung() di bawah ini
  # Hapus pass jika implementasi sudah dibuat

  #bilangan akan ditambahkan jika tidak ada operator yang ditulis dan jika operator ditulis '+'
  if (operator == '' or operator == '+'):
      hasil = bil1 + bil2
      return hasil
  #bilangan akan dikurangi jika operator ditulis '-'
  elif (operator == '-'):
      hasil = bil1 - bil2
      return hasil
  #dan bilangan akan dikalikan jika operator ditulis '*'
  elif (operator == '*'):
      hasil = bil1 * bil2
      return hasil


# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya
# (untuk fungsi hitung_kesamaan() dan fungsi hitung()).
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  print("Hasil cetak_nama('Mawar'):")
  cetak_nama("Mawar")
  print()
  print("Hasil cetak_nama(''):")
  cetak_nama("")
  print()
  r = hitung_kesamaan('python', 'path')
  print(f"hitung_kesamaan('python', 'path') = {r} \t(solusi: 3)")
  r = hitung_kesamaan('masak', 'cuci')
  print(f"hitung_kesamaan('masak', 'cuci') = {r} \t(solusi: 0)")
  r = hitung_kesamaan('python', '')
  print(f"hitung_kesamaan('python', '') = {r} \t\t(solusi: 0)")
  print()
  r = hitung(4, 8)
  print(f'hitung(4, 8) = {r} \t\t(solusi: 12)')
  r = hitung(4, 8, '-')
  print(f"hitung(4, 8, '-') = {r} \t(solusi: -4)")
  r = hitung(4, 8, '*')
  print(f"hitung(4, 8, '*') = {r} \t(solusi: 32)")

if __name__ == '__main__':
  test()