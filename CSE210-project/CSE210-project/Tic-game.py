print()
print(' Author: Adaobi Okudo')

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valid = False


def main():
    print(' welcome to Tictoe Game')
    PrintBoard()
    Turn()
  
# to print the  box number with the values from board#

def PrintBoard():
    print()
    print('', board[0], "|", board[1], "|", board[2])
    print("---|---|---")
    print('', board[3], "|", board[4], "|", board[5])
    print("---|---|---")
    print('', board[6], "|", board[7], "|", board[8])
    print()
 

# to get the players choices

def Turn(player):
      number = input("Choose a space from 1 to 9: ")
      valid = False
      while not valid:
         while number not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            number = input("Make sure the number is from 1-9! ")
         number = int(number)-1
         if board[number] == " ":
            valid = True
         else:
            print("Please try again, the one you chose is already taken! ")
      board[number] = player
      Turn(player)
         
def CheckWinner(player):
    count = 0
    for a in range(9):
      if board[a] == "X" or board[a] == "O":
        count += 1
      if count == 9:
        print("The game ends in a Tie\n")
        return True

    while not valid:
     
     PrintBoard()
     valid = CheckWinner("O")
     if valid == True:
      break
      print("Choose a box player X")
     Turn("X")

     PrintBoard()
     valid = CheckWinner(player)("X")
     if valid == True:
      break
      print("Choose a box player O")
      Turn("O")


main()



     
  




 