# magiczna kula 8

import random
import os


def magicball():
    print("Witaj w 8ball!")
    print("")
    print("Podaj imię: ")
    name = input()
    answer = ""
    error = "Serio nie podasz niczego?"

    print("Zadaj pytanie")
    question = input()

    random_number = random.randint(1, 10)

    if random_number == 1:
        answer = "Tak - Oczywiście!"
    elif random_number == 2:
        answer = "Tak też zostało postanowione"
    elif random_number == 3:
        answer = "Bez wątpienia"
    elif random_number == 4:
        answer = "Ziom, weź powtórz powoli"
    elif random_number == 5:
        answer = "Odpowiem Ci później"
    elif random_number == 6:
        answer = "Chyba wolę nie odpowiadać"
    elif random_number == 7:
        answer = "Źródełko mówi mi nie"
    elif random_number == 8:
        answer = "Chyba nie"
    elif random_number == 9:
        answer = "Powątpiewam"
    elif random_number == 10:
        answer = "No! You cannot!"
    else:
        print("Error")

    os.system('cls')
    if (name == "") and (question == ""):
        print(error)
    elif question == "":
        print("Musisz zadać pytanie jeśli chcesz znać odpowiedź")
    elif name == "":
        print("Pytanie: " + question)
        print(f"Magiczna kula nr 8 odpowiada: {answer}")
    else:
        print(name + " pyta: " + question)
        print(f"Magiczna kula nr 8 odpowiada: {answer}")

    os.system("pause")

    #def play_game_MK(self):
     #   pass