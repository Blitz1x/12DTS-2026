# -- File Name -- Tic Tac Toe
# -- Author -- Oliver Culbert
# -- Date -- 23/02/2026

# ------- Variables ------------
board = [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
]

player_one = "X"
player_two = "O"

# ------- Functions ----------
def print_board():
    for row in board:
        print(" ".join(row))
    print()



# --------- Start -------------
while True:
    print_board()
    print("Player One's turn ->", player_one)

    try:
        row = int(input("Enter row 1 -> 3"))
        column = int(input("Enter column 1 -> 3"))
    except ValueError:
        print("Please enter a valid number")
        continue

    if row not in range(1 - 3) or column not in range(1 - 3):
        print("Invalid Position, Try Again")