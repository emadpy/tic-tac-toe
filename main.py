

cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board():
    for idx, i in enumerate(cells):
        print(f"|{i}|", end="")
        if (idx + 1) % 3 == 0:
            print()


def update_board(player_input, symbol):
    cell_index = player_input - 1

    if cell_index < 0 or cell_index >= 9:
        print("Invalid move! Choose a number from 1 to 9.")
        return False
    elif isinstance(cells[cell_index], int):
            cells[cell_index] = symbol
            return True
    else:
        print("Can't place there! Cell already taken.")
        return False


def check_winner():
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for i in win_combinations:
        a, b, c = i
        
        if cells[a] == cells[b] == cells[c]:
            return cells[a]
        
    return None


def start_game():
    current_player = "X"
    while True:
        display_board()
        while True:
            try:
                player = int(input(f"{current_player}: "))
                if update_board(player, current_player):
                    break
                else:
                    display_board()
            except ValueError:
                print("Please enter a number from 1 to 9!")

        winner = check_winner()

        if winner:
            display_board()
            print(f"Player {winner} wins!")
            break

        if all(isinstance(cell, str) for cell in cells):
            display_board()
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"



if __name__ == "__main__":
    start_game()