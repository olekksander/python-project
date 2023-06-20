import random
import os
import sys

class PRS:

    def __init__(self, moves = "brak decyzji", move = "brak decyzji"):
        self._moves = moves
        self._move = move

    # Funkcja do wyboru ruchu przez komputer
    def computer_move(self):
        self._moves = ['Papier', 'Kamień', 'Nożyce']
        return random.choice(self._moves)

    # Funkcja do pobrania ruchu gracza
    def player_move(self):
        while True:
            self._move = input("Wybierz swój ruch - Papier, Kamień, czy Nożyce? ").capitalize()
            if self._move in ['Papier', 'Kamień', 'Nożyce']:
                return self._move
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

    # Funkcja porównująca ruchy gracza i komputera
    def compare_moves(self, player, computer):
        if player == computer:
            return "Remis!"
        elif player == 'Papier':
            if computer == 'Nożyce':
                return "Przegrałeś!"
            else:
                return "Wygrałeś!"
        elif player == 'Kamień':
            if computer == 'Papier':
                return "Przegrałeś!"
            else:
                return "Wygrałeś!"
        elif player == 'Nożyce':
            if computer == 'Kamień':
                return "Przegrałeś!"
            else:
                return "Wygrałeś!"

    # Funkcja uruchamiająca grę
    def play_game_PRS(self):
        print("Witaj w grze Papier-Kamień-Nożyce!")
        while True:
            player = self.player_move()
            computer = self.computer_move()
            result = self.compare_moves(player, computer)
            print(f"Ty wybrałeś: {player}. Komputer wybrał: {computer}.")
            print(result)
            play_again = input("Czy chcesz zagrać ponownie? (tak/nie) ").lower()
            if play_again == 'nie':
                break
            elif play_again == 'tak':
                continue
            else:
                print("Błędny wybór")
                while True:
                    play_again = input("Czy chcesz zagrać ponownie? (tak/nie) ").lower()
                    if play_again == 'nie':
                        print("Program się wyłączy.")
                        os.system("pause")
                        sys.exit()
                    elif play_again == 'tak':
                        break
                    else:
                        print("Błąd")