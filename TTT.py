import os

class TTT:
    def print_board(self, board):
        print("   |   |   ")
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {board[6]} | {board[7]} | {board[8]} ")
        print("   |   |   ")

    def get_move(self, player, board):
        valid_move = False
        while not valid_move:
            move = input(f"{player}, enter a position (1-9): ")
            if move.isdigit() and int(move) in range(1, 10) and board[int(move) - 1] == " ":
                valid_move = True
            else:
                print("Invalid move. Try again.")
        return int(move) - 1

    def check_win(self, board):
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for pos in win_positions:
            if board[pos[0]] == board[pos[1]] == board[pos[2]] != " ":
                return board[pos[0]]
        if " " not in board:
            return "tie"
        return None

    def play_game_TTT(self):
        board = [" "] * 9
        players = ["X", "O"]
        current_player = 0
        winner = None
        while not winner:
            self.print_board(board)
            move = self.get_move(players[current_player], board)
            board[move] = players[current_player]
            winner = self.check_win(board)
            current_player = (current_player + 1) % 2
        self.print_board(board)
        if winner == "tie":
            print("It's a tie!")
        else:
            print(f"{winner} wins!")
        os.system("pause")