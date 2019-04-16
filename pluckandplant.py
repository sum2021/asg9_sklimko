//Summer Klimko
kangaroo = [0,0]
flower = [0,3]

board = []
for i in range(5):
    board.append(["0"] * 5)

kangaroo = "k"
flower = "*"
flowerCol = 0
flowerRow = 3
board[flowerRow][flowerCol] = flower
previousR = 3
previousC = 0
board[0][0] = kangaroo
previousKangRow = 0
previousKangCol = 0

def printBoard(board):
  for row in board:
    print(' '.join(row))

printBoard(board)
moves = 0

while(moves<=4):
    flowerMovRow = int(input("enter the row :: "))
    flowerMovCol =  int(input("enter the column :: "))
    if((flowerMovRow > 4 or flowerMovRow < 0) or (flowerMovCol > 4 or flowerMovCol < 0 )):
        print("Not valid coordinates, try again")
        continue
    board[flowerMovRow][flowerMovCol] = flower
    board[previousR][previousC] = "0"
    print("before kangaroo catches the flower")
    printBoard(board)
    board[flowerMovRow][flowerMovCol] = kangaroo
    board[previousKangRow][previousKangCol] = "0"
    print("\n")
    print("after kangaroo catches the flower")
    printBoard(board)
    previousR = flowerMovRow
    previousCol = flowerMovCol
    previousKangRow = flowerMovRow
    previousKangCol  = flowerMovCol
    print("The kangaroo caught the flower again, where would you like to plant it?")
    moves+=1

print("Thanks for playing!")
