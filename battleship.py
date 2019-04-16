from random import randint

#initializing board
board = []

for x in range(5):
    board.append(["0"]*5)

def print_board(board):
    for row in board:
        print (' '.join(row))

#starting the game and printing the board
print("Let's play Battleship!")
print_board(board)

#defining where the ship is
def random_row(board):
    return randint(0, len(board-1))
def random_col(board):
    return randint(0, len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)

#asking the user for a guess
for turn in range(4):
    guess_row = int(input("Guess row:"))
    guess_col = int(input("Guess Column:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my ship")
        break
    else:
        if(guess_row < 0 or guess_row > 4):
            print("oops, try again")
        
    