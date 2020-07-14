from random import randint
import os

clear = lambda: os.system('cls')

#creates board
def create_board():
    board = []
    for x in range(0, 5):
      board.append(["O"] * 5)
    return board

##Prints Board
def print_board(b):
  print (" ")
  s = " "
  for row in b:
      print (s.join(row))

##Random CPU Ship Placemnt##
def random_row(b):
  return randint(1, len(b) - 2)

def random_col(b):
  return randint(1, len(b[0]) - 2)

def place_ship_x(b):
    ship_col = random_col(b)
    return ship_col

def place_ship_y(b):
    ship_row = random_row(b)
    return ship_row

##initalize ship list of coordinates##
def ship_place(row, col):
    ship_list = []
    ##generates additional ship coordinates##
    ship_orient = randint(0,1)
    if ship_orient == 0:
        ship_list = [[row - 1, col], [row, col], [row + 1, col]]
    elif ship_orient == 1:
        ship_list = [[row, col - 1], [row, col], [row, col + 1]]
    ##comment prints full location of ship
    #print (ship_list)
    return ship_list

####################Game Loop#########################

def game():
    board = create_board()
    print_board(board)
    ship_x = place_ship_x(board)
    ship_y = place_ship_y(board)
    ship_coor = ship_place(ship_y, ship_x)
    total_hits = 0
    misses = 0

    while misses != 5:
      print (" ")
      if misses == 0:
        print ("You are allowed 5 misses")

      print ("Total Misses = ", misses)
      print (" ")

      ##user guess##
      ship_part = []
      guess_row = int(input("Guess Row: "))
      guess_col = int(input("Guess Col: "))
      ship_part.append(guess_row)
      ship_part.append(guess_col)

      ##handler for different guess cases##
      if ship_part in ship_coor:
        print ("Hit! \n")
        board[guess_row][guess_col] = "H"
        total_hits += 1
        ##Winning Case##
        if total_hits == len(ship_coor):
            print_board(board)
            print ("Congratulations! You sunk my battleship")
            break
      else:
        ##off board##
        if guess_row not in range(5) or \
          guess_col not in range(5):
          print ("Oops, that's not even in the ocean.")
          print ("Guess again! \n")
        ##repeat guess##
        elif board[guess_row][guess_col] == "X":
          print ("You guessed that one already.")
          print ("Guess again! \n")
        ##miss##
        else:
          print ("You missed my battleship! \n")
          board[guess_row][guess_col] = "X"
          misses += 1

      ##reprint board for next turn##
      print_board(board)

      ##One miss Remaining##
      if misses == 4:
        print ("One Miss Remaining!")

      ##Losing Case##
      if misses == 5:
        print ("Game Over")
        print ("Ship was at:")
        print (ship_coor)
        break

#play again loop
def main():
    play = True
    while play:
        game()
        play = 'y' in input("Play Again? (y/n)").lower()
        clear()
main()
