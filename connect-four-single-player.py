print("Connect Four")
print(" ")

top_numbers = ["A", "B", "C", "D", "E", "F", "G"]

board = [["","","","","","",""], 
         ["","","","","","",""], 
         ["","","","","","",""], 
         ["","","","","","",""], 
         ["","","","","","",""], 
         ["","","","","","",""]]

rows = 6
columns = 7

def print_board():
  print("\n     A    B    C    D    E    F    G  ")
  for i in range(rows):
    print("   +----+----+----+----+----+----+----+")
    print(i, " |", end="")
    for x in range(columns):
      if(board[i][x] == "🔴"):
          print(" " + board[i][x], end=" |")
      elif(board[i][x] == "🟡"):
          print(" " + board[i][x], end=" |")
      else:
          print("   ", end=" |")
    print()
  print("   +----+----+----+----+----+----+----+")

def modify_turn(space_picked, turn):
  board[space_picked[0]][space_picked[1]] = turn

def check_winner(chip):
  # Horizontal
  for r in range(rows):
    for c in range(columns-3):
      if(board[r][c] == chip and board[r][c+1] == chip and 
         board[r][c+2] == chip and board[r][c+3] == chip):
        print("\nGame Over!", chip, "wins! Thanks for playing!")
        return True

  # Vertical
  for r in range(rows-3):
    for c in range(columns):
      if(board[r][c] == chip and board[r+1][c] == chip and 
         board[r+2][c] == chip and board[r+3][c] == chip):
        print("\nGame Over!", chip, "wins! Thanks for playing!")
        return True

  # Diagonal /
  for r in range(3, rows):
    for c in range(columns-3):
      if(board[r][c] == chip and board[r-1][c+1] == chip and 
         board[r-2][c+2] == chip and board[r-3][c+3] == chip):
        print("\nGame Over!", chip, "wins! Thanks for playing!")
        return True

  # Diagonal \
  for r in range(rows-3):
    for c in range(columns-3):
      if(board[r][c] == chip and board[r+1][c+1] == chip and 
         board[r+2][c+2] == chip and board[r+3][c+3] == chip):
        print("\nGame Over!", chip, "wins! Thanks for playing!")
        return True

  return False

def coordinate_parser(input_string):
  col_dict = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6}
  return [None, col_dict.get(input_string.upper(), None)]

def get_next_open_row(col):
  for r in range(rows-1, -1, -1):  # start from bottom row
    if board[r][col] == "":
      return r
  return None

# ---- Main Game Loop ----
turn_counter = 0
game_over = False

print_board()

while not game_over:
  player = "🔴" if turn_counter % 2 == 0 else "🟡"
  choice = input(f"\nPlayer {player}, choose a column (A-G): ").upper()

  if choice not in top_numbers:
    print("Invalid column! Pick A-G.")
    continue

  coords = coordinate_parser(choice)
  col = coords[1]

  row = get_next_open_row(col)
  if row is None:
    print("Column is full! Pick another one.")
    continue

  modify_turn([row, col], player)
  print_board()

  if check_winner(player):
    game_over = True
    break

  # Check draw
  if all(board[0][c] != "" for c in range(columns)):
    print("\nIt's a draw! Thanks for playing!")
    game_over = True
    break

  turn_counter += 1
