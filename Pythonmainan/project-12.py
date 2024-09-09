# Input waktu J1 dan J2
J1 = input("Masukkan waktu J1 (format /1/1:mm:ss): ")
J2 = input("Masukkan waktu J2 (format /1/J:mm:ss): ")

# Memisahkan komponen waktu
jam1, menit1, detik1 = map(int, J1.split(':')[1].split('/')[1:])
jam2, menit2, detik2 = map(int, J2.split(':')[1].split('/')[1:])

# Menghitung total detik dari masing-masing waktu
total_detik_J1 = jam1 * 3600 + menit1 * 60 + detik1
total_detik_J2 = jam2 * 3600 + menit2 * 60 + detik2

# Menghitung selisih waktu
selisih_detik = total_detik_J2 - total_detik_J1

# Mengonversi kembali ke format jam:menit:detik
jam_selisih = selisih_detik // 3600
menit_selisih = (selisih_detik % 3600) // 60
detik_selisih = selisih_detik % 60

# Menampilkan hasil
print(f"Selisih waktu adalah: {jam_selisih}:{menit_selisih}:{detik_selisih}")