import random

def roll_dice(sides):
    return random.randint(1, sides)

while True:
    print("Options:")
    print("Ketik 'roll' untuk melempar dadu")
    print("Ketik 'exit' untuk mengakhiri program")

    user_input = input(": ")

    if user_input == "exit":
        break

    if user_input == "roll":
        sides = int(input("Masukkan jumlah sisi pada dadu: "))
        result = roll_dice(sides)
        print(f"Kamu Melempar dadu {sides}-sisi dan mendapat: {result}")
    else:
        print("Invalid input. Please enter a valid option.")