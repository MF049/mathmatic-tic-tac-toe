# welcome to mathmatic tic-tac-toe game 
# author : Mohamed FathElrahman Osman
# I did my best in this project
 
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True
winner = None
odd = [1, 3, 5, 7, 9]
even = [0, 2, 4, 6, 8]
print("player_1 goes first with odd numbers: ",odd)
print("player_2 goes second with even numbers: ",even)

current_player = "player_1"


def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        # flip to the other player
        flip_player()
 

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):
    print(player + "'s turn.")
    global game_still_going

    position = input("Choose a position from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:
        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == "-":
            valid = True
         
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    choice = input("choose your number: ")
    choice_int = int(choice)
    board[position] = choice
    #while  valid:
    while choice_int in odd or choice_int in even :
            if current_player == "player_1" and choice_int in odd:
                odd.remove(choice_int)
                print(odd)
             
            elif current_player == "player_2" and choice_int in even:
                even.remove(choice_int)
                print(even) 
            else:
              handle_turn(current_player)

 

    display_board()
     
 
def check_if_game_over():
    global winner
    check_for_winner()
    check_tie()

    return winner


def check_for_winner():
    global winner
    check_rows()
    check_columns()
    check_diagonals()
    check_tie()
    return winner


def check_rows():
    global game_still_going
    global winner
    global current_player

    ## while loop or for loop here to update the values in every time
    sum_row_1 = 0
    sum_row_2 = 0
    sum_row_3 = 0
    while game_still_going:

        row_1 = board[0] + board[1] + board[2]

        if board[0] != "-" and board[1] != "-" and board[2] != "-":
            for x in range(3):
                sum_row_1 += int(row_1[x])
            if sum_row_1 == 15:
                winner = current_player
                game_still_going = False
                print( winner , "won")
                break

        row_2 = board[3] + board[4] + board[5]
        if board[3] != "-" and board[4] != "-" and board[5] != "-":
            for x in range(3):
                sum_row_2 += int(row_2[x])

            if sum_row_2 == 15:
                winner = current_player
                game_still_going = False
                print( winner , "won")
                break

        row_3 = board[6] + board[7] + board[8]
        if board[6] != "-" and board[7] != "-" and board[8] != "-":
            for x in range(3):
                sum_row_3 += int(row_3[x])
            if sum_row_3 == 15:
                winner = current_player
                game_still_going = False
                print( winner , "won")
                break
        else:
            return None


def check_columns():
    global game_still_going
    global winner
    global current_player

    ## while loop or for loop here to update the values in every time
    sum_column_1 = 0
    sum_column_2 = 0
    sum_column_3 = 0
    while game_still_going:

        column_1 = board[0] + board[3] + board[6]

        if board[0] != "-" and board[3] != "-" and board[6] != "-":
            for x in range(3):
                sum_column_1 += int(column_1[x])
            if sum_column_1 == 15:
                winner = current_player
                game_still_going = False
                print( winner , "won")
                break

        column_2 = board[1] + board[4] + board[7]
        if board[1] != "-" and board[4] != "-" and board[7] != "-":
            for x in range(3):
                sum_column_2 += int(column_2[x])

            if sum_column_2 == 15:
                winner = current_player
                game_still_going = False
                print( winner , "won")
                break

        column_3 = board[2] + board[5] + board[8]
        if board[2] != "-" and board[5] != "-" and board[8] != "-":
            for x in range(3):
                sum_column_3 += int(column_3[x])
            if sum_column_3 == 15:
                winner = current_player
                game_still_going = False
                print( winner , "won")
                break
        else:
            return None


def check_diagonals():
    global game_still_going
    global winner
    global current_player

    ## while loop or for loop here to update the values in every time
    sum_diagonal_1 = 0
    sum_diagonal_2 = 0

    while game_still_going:

        diagonal_1 = board[0] + board[4] + board[8]

        if board[0] != "-" and board[4] != "-" and board[8] != "-":
            for x in range(3):
                sum_diagonal_1 += int(diagonal_1[x])
            if sum_diagonal_1 == 15:
                winner = current_player
                game_still_going = False
                print( winner , "won")
                break

        diagonal_2 = board[2] + board[4] + board[6]
        if board[2] != "-" and board[4] != "-" and board[6] != "-":
            for x in range(3):
                sum_diagonal_2 += int(diagonal_2[x])

            if sum_diagonal_2 == 15:
                winner = current_player
                game_still_going = False
                print( winner , "won")
                break

        else:
            return None 


def check_tie():
    # Set global variables
    global game_still_going
    # If board is full
    if "-" not in board:
        game_still_going = False
        print("tie")
        return True
    # Else there is no tie
    else:
        return False


def flip_player():
    # Global variables we need
    global current_player
    
    # If the current player was player_1, make it player_2
    if current_player == "player_1":
        current_player = "player_2"
    # Or if the current player was player_2, make it player_1
    else:
        current_player = "player_1"


play_game()
end_game = input("enter 1 to exis : ") 

