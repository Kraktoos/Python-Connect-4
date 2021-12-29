# -------------------
# Code by Kraktoos
# github.com/kraktoos
# -------------------

import os, time

player_one = ""
player_two = ""
moves = 0
col = 0

board = [[" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear()
    print("-----------------------")
    print("What do you want to do?")
    print("Type \"Q\" to quit.\nType \"P\" to play.")
    print("-----------------------")
    answer = input("> ")
    if answer.lower() == "q":
        clear()
        print("Quitting")
        quit()
    elif answer.lower() == "p":
        play_two_players()
    else:
        clear()
        print("Invalid Answer.\nPlease repeat your request.")
        time.sleep(3)
        main_menu()

def print_board():
    clear()
    global board
    for i in range(0, 6):
        print(board[i][0] + " | " + board[i][1] + " | " + board[i][2] + " | " + board[i][3] + " | " + board[i][4] + " | " + board[i][5] + " | " + board[i][6])
    print("--|---|---|---|---|---|--")
    print("1 | 2 | 3 | 4 | 5 | 6 | 7 ")

def check_for_win():
    global board, player_one, player_two

    # Horizontal Checks
    for i in range(6):
        for j in range(4):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] and board[i][j] != " ":
                clear()
                print_board()
                if board[i][j] == "X":
                    print(f"Player 1 ({player_one}) Won")
                else:
                    print(f"Player 2 ({player_two}) Won")
                print("Type \"A\" to play again.")
                print("Type \"Q\" to quit.")
                answer = input("> ")
                if answer.lower() == "a":
                    play_two_players()
                elif answer.lower() == "q":
                    clear()
                    print("Quitting")
                    quit()
                else:
                    main_menu()
                return True

    # Vertical Checks
    for i in range(3):
        for j in range(7):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] and board[i][j] != " ":
                clear()
                print_board()
                if board[i][j] == "X":
                    print(f"Player 1 ({player_one}) Won")
                else:
                    print(f"Player 2 ({player_two}) Won")
                print("Type \"A\" to play again.")
                print("Type \"Q\" to quit.")
                answer = input("> ")
                if answer.lower() == "a":
                    play_two_players()
                elif answer.lower() == "q":
                    clear()
                    print("Quitting")
                    quit()
                else:
                    main_menu()
                return True
    
    # Downwards Checks
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] and board[i][j] != " ":
                clear()
                print_board()
                if board[i][j] == "X":
                    print(f"Player 1 ({player_one}) Won")
                else:
                    print(f"Player 2 ({player_two}) Won")
                print("Type \"A\" to play again.")
                print("Type \"Q\" to quit.")
                answer = input("> ")
                if answer.lower() == "a":
                    play_two_players()
                elif answer.lower() == "q":
                    clear()
                    print("Quitting")
                    quit()
                else:
                    main_menu()
                return True

    # Upwards Checks
    for i in range(3, 6):
        for j in range(4):
            if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] and board[i][j] != " ":
                clear()
                print_board()
                if board[i][j] == "X":
                    print(f"Player 1 ({player_one}) Won")
                else:
                    print(f"Player 2 ({player_two}) Won")
                print("Type \"A\" to play again.")
                print("Type \"Q\" to quit.")
                answer = input("> ")
                if answer.lower() == "a":
                    play_two_players()
                elif answer.lower() == "q":
                    clear()
                    print("Quitting")
                    quit()
                else:
                    main_menu()
                return True

def place_piece(col = 0):
    global board, moves, player_one, player_two

    if moves % 2 + 1 == 1:
        print(f"\nCurrent Player: 1 ({player_one})")
    else:
        print(f"\nCurrent Player: 2 ({player_two})")
    print("Where do you want to play? (choose a column)")
    col = int(input("> ")) - 1

    if moves % 2 + 1 == 1:
        player = "X"
    else:
        player = "O"

    for i in range(5, -1, -1):
        if board[i][col] == " ":
            board[i][col] = player
            break
    else:
        print("That Column is Full")
        time.sleep(1)
        clear()
        print_board()
        place_piece(col)
    clear()


def play_two_players():
    global player_one, player_two, moves, col
    clear()
    player_one = input("What is the name of the player one? (X)\n> ")
    clear()
    player_two = input("What is the name of the player two? (O)\n> ")

    while True:
        print_board()
        place_piece()
        moves += 1
        if check_for_win():
            break


if __name__ == "__main__":
    main_menu()