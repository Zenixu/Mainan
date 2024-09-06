# Input nomor bulan dan tahun
bulan = int(input("Masukkan nomor bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

# Menentukan jumlah hari dalam bulan
if bulan == 2:
    if (tahun % 4 == 0 and tahun % 100 != 0) :
        hari = 29  # Tahun kabisat
    else:
        hari = 28  # Bukan tahun kabisat
elif bulan in [4, 6, 9, 11]:
    hari = 30  # Bulan dengan 30 hari
else:
    hari = 31  # Bulan dengan 31 hari

# Menampilkan hasil
print(f"Jumlah hari dalam bulan {bulan} tahun {tahun} adalah {hari}.")