# DDP LAB-2

# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini
print("Soal No. 1- Mencetak Bilangan")
for i in range(100, 1, -1):
	print(i)
print()

# SOAL 2 - Menghitung rata-rata
# Tuliskan program untuk Soal 2 di bawah ini

print("Soal No. 2 - Menghitung Rata-rata")
num = int(input("Masukan banyaknya angka: "))
total = 0
for i in range(num):
	a = int(input("Masukan angka: "))
	total = total + a
print("Rata-rata: ", total / num)
print()

# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini

print("Soal No. 3 Mencetak Persegi")
x = int(input("Masukan bilangan bulat: "))
for i in range(x):
	print(sep='')
	for j in range(x):
		print('#', end=' ')
