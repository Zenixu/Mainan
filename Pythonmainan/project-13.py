tanggal1 = input("Masukkan tanggal pertama (dd:mm:yy): ")
tanggal2 = input("Masukkan tanggal kedua (dd:mm:yy): ")

dd1, mm1, yy1 = map(int, tanggal1.split(':'))
dd2, mm2, yy2 = map(int, tanggal2.split(':'))

total_hari1 = (yy1 * 365) + (mm1 * 30) + dd1
total_hari2 = (yy2 * 365) + (mm2 * 30) + dd2

selisih_hari = abs(total_hari1 - total_hari2)

tahun = selisih_hari // 365
sisa_hari = selisih_hari % 365
bulan = sisa_hari // 30
hari = sisa_hari % 30

print(f"Jarak antara kedua tanggal adalah: {tahun} tahun, {bulan} bulan, {hari} hari.")
