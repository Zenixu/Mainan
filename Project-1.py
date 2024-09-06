import random
#cetak intruksi multiline
#melakukan penggabungan string dari string
print('aturan pemenangkan permainan Gunting Batu Kertas adalah :\n'
    + "Batu vs Kertas -> Kertas Menang \n"
    + "Batu vs Gunting -> Batu Menang \n"
    + "Kertas vs Gunting -> Gunting Menang \n")

while True:

    print("Tentukan Pilihanmu \n 1 - Batu \n 2 - Kertas \n 3 - Gunting \n")

    choice = int(input("Tentukan Pilihanmu :"))
    while choice > 3 or choice < 1:
        choice = int(input('PILIHANNYA 123 DOANG YA!!! ☺'))
    
    if choice == 1:
        choice_name = 'Batu'
    elif choice == 2:
        choice_name = 'Kertas'
    else:
        choice_name = 'Gunting'

        # print user choice
    print('Player sedang memilih  \n', choice_name)
    print('Sekarang giliran computer memilih....')

    # Komputer memilih nomor yang acak
    # among 1 , 2 and 3. Using randint method

    comp_choice = random.randint(1, 3)

    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Batu'
    elif comp_choice == 2:
        comp_choice_name = 'Kertas'
    else:
        comp_choice_name = 'Gunting'
    print("Pilihan komputer adalah \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    # we need to check of a draw
    if choice == comp_choice:
        print('Hasil Seri', end="")
        result = "SERI"
    # condition for winning
    if (choice == 1 and comp_choice == 2):
        print('KERTAS MENANG =>', end="")
        result = 'Kertas'
    elif (choice == 2 and comp_choice == 1):
        print('KERTAS MENANG =>', end="")
        result = 'Kertas'

    if (choice == 1 and comp_choice == 3):
        print('BATU MENANG =>\n', end="")
        result = 'Batu'
    elif (choice == 3 and comp_choice == 1):
        print('BATU MENANG =>\n', end="")
        result = 'Batu'

    if (choice == 2 and comp_choice == 3):
        print('GUNTING MENANG =>', end="")
        result = 'Gunting'
    elif (choice == 3 and comp_choice == 2):
        print('GUNTING MENANG =>', end="")
        result = 'Batu'
        
    if result == 'SERI':
        print("\n <== YAHH SERII ==>")
    if result == choice_name:
        print("\n <== Kamu menang ==>")
    else:
        print("\n<== Komputer menang ==>")
    print("MAIN LAGI? KLIKK AJA Y KALAU MAU UDAHAN KLIK N (Y/N)")
    
    ans = input().lower()
    if ans == 'n':
        break

print("Hatur nuhunn udaa mainn")