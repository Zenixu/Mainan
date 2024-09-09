# Membaca tinggi badan dari pengguna
tinggi_badan = float(input("Masukkan tinggi badan (dalam cm): "))

# Menghitung berat badan ideal
berat_badan_ideal = tinggi_badan - 100
berat_badan_ideal -= 0.1 * berat_badan_ideal

# Menampilkan hasil
print("Berat badan ideal untuk tinggi badan", tinggi_badan, "cm adalah:", round(berat_badan_ideal, 2), "kg")