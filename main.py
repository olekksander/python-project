import os
import sys

from TTT import TTT
from PRS import  PRS
from magicball import magicball

while True:
    ans = input("W co chcesz zagrać? MK8 - magicball, PRS - papier kamień nożyce, TTT- tic-tac-toe. Aby wyjść wpisz 'exit'. ")

    if ans == "TTT" or ans == "ttt":
        while True:
            gameone = TTT()
            gameone.play_game_TTT()
            play_again = input("Czy chcesz zagrać ponownie? (tak/nie) ").lower()
            if play_again == 'nie':
                break
            elif play_again == 'tak':
                continue
            elif play_again != 'tak' and play_again != 'nie':
                print("Błędny wybór")
                while True:
                    play_again = input("Czy chcesz wybrać ponownie? (tak/nie) ").lower()
                    if play_again == 'nie':
                        print("Program się wyłączy.")
                        os.system("pause")
                        sys.exit()
                    elif play_again == 'tak':
                        break
                    else:
                        print("Błąd")
                        # os.system("pause")
                        # break
            else:
                print("error")
                os.system("pause")
    elif ans == "PRS" or ans == "prs":
        gametwo = PRS()
        gametwo.play_game_PRS()
        #w tym miejscu play_again nie działa, pozostawione dla siebie na przyszłość
        #play_again = input("Czy chcesz zagrać ponownie? (tak/nie) ").lower()
        #if play_again == 'nie':
        #    break
        #elif play_again == 'tak':
        #    print("Ponowny wybór")
        #else:
        #    print("Błędny wybór")
    elif ans == "MK8" or ans == "mk8":
        while True:
            gamethree = magicball()
            #gamethree.play_game_MK()
            play_again = input("Czy chcesz zagrać ponownie? (tak/nie) ").lower()
            if play_again == 'nie':
                break
            elif play_again == 'tak':
                continue
            elif play_again != 'tak' and play_again != 'nie':
                print("Błędny wybór")
                while True:
                    play_again = input("Czy chcesz wybrać ponownie? (tak/nie) ").lower()
                    if play_again == 'nie':
                        print("Program się wyłączy.")
                        os.system("pause")
                        sys.exit()
                    elif play_again == 'tak':
                        break
                    else:
                        print("Błąd")
                        #os.system("pause")
                        #break
            else:
                print("error")
                os.system("pause")
    elif ans == "exit":
        break
    elif ans != "TTT" and ans != "ttt" and ans != "PRS" and ans != "prs" and ans != "MK8" and ans != "mk8":
        print("Błędny wybór!")
        play_again = input("Czy chcesz wybrać ponownie? (tak/nie) ").lower()
        if play_again == 'nie':
            break
        elif play_again == 'tak':
            continue
        else:
             print("Błąd")
             while True:
                 play_again = input("Czy chcesz wybrać ponownie? (tak/nie) ").lower()
                 if play_again == 'nie':
                     sys.exit()
                 elif play_again == 'tak':
                     break
                 else:
                     print("Błąd")
             #os.system("pause")
             #break
    else:
        print("")
        print("Błędny wybór")
        play_again = input("Czy chcesz wybrać ponownie? (tak/nie) ").lower()
        if play_again == 'nie':
            break
        elif play_again == "tak":
            print("Ponowny wybór")
        else:
            print("Błędna odpowiedź")
            play_again = input("Czy chcesz wybrać ponownie? (tak/nie) ").lower()