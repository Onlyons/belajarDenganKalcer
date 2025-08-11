# Kalkulator Sederhana

print("=== Kalkulator Python ===")
print("Pilih operasi:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

# Input pilihan
pilihan = input("Masukkan pilihan (1/2/3/4): ")

# Input angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Proses operasi
if pilihan == '1':
    hasil = angka1 + angka2
    print(f"Hasil: {hasil}")
elif pilihan == '2':
    hasil = angka1 - angka2
    print(f"Hasil: {hasil}")
elif pilihan == '3':
    hasil = angka1 * angka2
    print(f"Hasil: {hasil}")
elif pilihan == '4':
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {hasil}")
    else:
        print("Error: Pembagian dengan nol!")
else:
    print("Pilihan tidak valid!")
