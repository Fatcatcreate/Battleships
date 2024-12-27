import sys
import random
r = open("Record.txt", "a")
choice = int(input("Would you like to play Battleships or Battlefield? Type 1 or 2"))
if choice == 2:

  WIDTH = 10
  HEIGHT = 5
  print("""============== ASCII BATTLEFIELD GAME =============

Instructions:
- You are represented by the '@' symbol.
- The enemy is represented by the 'X' symbol.
- Move around the battlefield using the arrow keys.
- Defeat the enemy by reaching its position.

Legend:
@ - Player
X - Enemy
. - Empty space

===================================================

##########
#........#
#..X.....#
#........#
##########

===================================================

Game started! Defeat the enemy!""")

  r.write("""============== ASCII BATTLEFIELD GAME =============

         Instructions:
         - You are represented by the '@' symbol.
         - The enemy is represented by the 'X' symbol.
         - Move around the battlefield using the arrow keys.
         - Defeat the enemy by reaching its position.

         Legend:
         @ - Player
         X - Enemy
         . - Empty space

         ===================================================

         ##########
         #........#
         #..X.....#
         #........#
         ##########

         ===================================================

         Game started! Defeat the enemy!""")


  g = random.randint(1,9)
  f = random.randint(1,4)
  player_pos = [1, 1]
  enemy_pos = [g, f]

  def draw_battlefield():

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if [x, y] == player_pos:
                print("@", end="")
                r.write("@",end="")
            elif [x, y] == enemy_pos:
                print("X", end="")
                r.write("X", end="")
            else:
                print(".", end="")
                r.write(".", end ="")
        print()
        r.write()
  def move_player(direction):

    x, y = player_pos

    if direction == "up" and y > 0:
        player_pos[1] -= 1
    elif direction == "down" and y < HEIGHT - 1:
        player_pos[1] += 1
    elif direction == "left" and x > 0:
        player_pos[0] -= 1
    elif direction == "right" and x < WIDTH - 1:
        player_pos[0] += 1
  def move_comp():
   e = random.randint(1,4)
   if e == 1 and f > 0:
        enemy_pos[1] -= 1
   elif e == 2 and f < HEIGHT - 1:
        enemy_pos[1] += 1
   elif e == 3 and g > 0:
        enemy_pos[0] -= 1
   elif e == 4 and g < WIDTH - 1:
       enemy_pos[0] += 1

  def play_game():

    draw_battlefield()

    while True:
        move = input("Enter your move (up/down/left/right): ")
        move_comp()
        move_player(move)
        draw_battlefield()

        if player_pos == enemy_pos:
            print("Congratulations! You defeated the enemy!")
            r.write("Congratulations! You defeated the enemy!")
            break

  if __name__ == "__main__":
    play_game()

if choice == 1:


  def create_grid():
    return [[' ' for _ in range(10)] for _ in range(10)]


  def print_grid(grid):
      
    print('   A B C D E F G H I J')
    for i in range(10):
        print(f'{i}  {" ".join(grid[i])}')

  def place_ship(grid, ship, row, col, direction):
    length = len(ship)
    if direction == 'V':
        for i in range(length):
            grid[row+i][col] = 'O'
    elif direction == 'H':
        for i in range(length):
            grid[row][col+i] = 'O'


  def can_place_ship(grid, ship, row, col, direction):
    length = len(ship)
    if direction == 'V':
        if row + length > 10:
            return False
        for i in range(length):
            if grid[row+i][col] != ' ':
                return False
    elif direction == 'H':
        if col + length > 10:
            return False
        for i in range(length):
            if grid[row][col+i] != ' ':
                return False
    return True


  def place_computer_ships(grid):
    ships = [('Carrier', 5), ('Battleship', 4), ('Cruiser', 3), ('Submarine', 3), ('Destroyer', 2)]
    for ship, length in ships:
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            direction = random.choice(['V', 'H'])
            if can_place_ship(grid, [1] * length, row, col, direction):
                place_ship(grid, [1] * length, row, col, direction)
                break


  def convert_input_to_coords(input_str):
    col = ord(input_str[0].upper()) - ord('A')
    row = int(input_str[1:])
    return row, col


  def check_shot(grid, row, col):
    if grid[row][col] == 'O':
        grid[row][col] = 'X'
        return True
    elif grid[row][col] == ' ':
        grid[row][col] = '*'
        return False
  def computer_turn(player_grid,ship_hits,array,possibilities):
    c=len(ship_hits)
    if ship_hits[c-1][0]==0 or c<2:
      target=random.choice(array)
      row=array[target][0]
      col=array[target][1]
    elif ship_hits[c-1][0]==1:
      direction = random.choice(possibilities)
      if direction == 1:
        col=ord([c-1][2]) - ord('A')+1
        row = [c-1][1]
      elif direction == 2:
        col=ord([c-1][2]) - ord('A')-1
        row = [c-1][1]
      elif direction == 3:
        col=ord([c-1][2]) - ord('A')
        row1 = [c-1][1]
        row=row1-1
      elif direction == 4:
        col=ord([c-1][2]) - ord('A')
        row1 = [c-1][1]
        row=row1+1
    elif ship_hits[c-1][0]=='1verdown':
      row1=[c-1][1]
      row = row1+1
      col= ord([c-1][2]) - ord('A')

    elif ship_hits[c-1]=='1verup':
      row1=[c-1][1]
      row = row1-1
      col = ord([c-1][2]) - ord('A')

    elif ship_hits[c-1]=='1horlef':
      col=ord([c-1][2]) - ord('A')-1
      row = [c-1][1]
      
    elif ship_hits[c-1]=='1horrig':
      col=ord([c-1][2]) - ord('A')+1
      row= [c-1][1]

    hit = check_shot(player_grid, row, col)
    if hit:
        print(f"The computer hit your ship at {chr(col + ord('A'))}{row}")
        r.write(f"The computer hit your ship at {chr(col + ord('A'))}{row}")
        if ship_hits[c-1][0]==0:
          ship_hits.append([1,row,col])
        if ship_hits[c-1][0]!=0:
          if ship_hits[c-1][1]==1:
            if direction == 1:
              ship_hits.append(['1horrig',row,col])
            elif direction == 2:
              ship_hits.append(['1horlef',row,col])
            elif direction == 3:
              ship_hits.append(['1verup',row,col])
            elif direction == 4:
              ship_hits.append(['1verdown',row,col])
          if ship_hits[c-1][0]=='1horrig':
            ship_hits.append(['1horrig',row,col])
          elif ship_hits[c-1][0]=='1horrlef':
            ship_hits.append(['1horrlef',row,col])
          elif ship_hits[c-1][0]=='1verup':
            ship_hits.append(['1verup',row,col])
          elif ship_hits[c-1][0]=='1verdown':
            ship_hits.append(['1verdown',row,col])
          possibilties=[1,2,3,4]
        if check_game_over(player_grid):
            print("Oh no! The computer sunk all of your ships. You lose!")
            r.write("Oh no! The computer sunk all of your ships. You lose!")
    else:
        print(f"The computer missed at {chr(col + ord('A'))}{row}")
        r.write(f"The computer missed at {chr(col + ord('A'))}{row}")
        ship_hits.append([0,row,col])
        if ship_hits[c-1][0]==1:
          directions=[1,2,3,4]
          if direction == 1:
            possibilities.remove(1)
            ship_hits.append([1,ship_hits[c-1][1],ship_hits[c-1][2]])
          
          
        elif ship_hits[c-1][0]=='1verup' or ship_hits[c-1][0]=='1verdown' or ship_hits[c-1][0]=='1horrig' or ship_hits[c-1][0]=='1horlef':
          for i in range (len(ship_hits)):
            c = len(ship_hits)
            if ship_hits[c-i][0]==0:
              first_hit=c-i+1
              for i in range(c):
                if ship_hits[first_hit+i][0]=='1horrig' or ship_hits[first_hit+i][0]=='1horlef' or ship_hits[first_hit+i][0]=='1verup' or ship_hits[first_hit+i][0]=='1verdown':
                  direction_hit=first_hit+i
                  break
              if ship_hits[direction_hit][0]=='1horrig':
                ship_hits.append(['1horlef',ship_hits[direction_hit][1],ship_hits[direction_hit][2]])
              elif ship_hits[direction_hit][0]=='1horrlef':
                ship_hits.append(['1horrig',ship_hits[direction_hit][1],ship_hits[direction_hit][2]])
              elif ship_hits[direction_hit][0]=='1verup':
                ship_hits.append(['1verdown',ship_hits[direction_hit][1],ship_hits[direction_hit][2]])
              elif ship_hits[direction_hit][0]=='1verdown':
                ship_hits.append(['1verup',ship_hits[direction_hit][1],ship_hits[direction_hit][2]])
  
    return ship_hits,possibilties
                
  def check_game_over(grid):
    for row in grid:
        if 'O' in row:
            return False
    return True


  def play_game():
    ship_hits = []
    array=[[1,1],[3,1],[5,1],[7,1],[9,1],[2,2],[4,2],[6,2],[8,2],[10,2],[1,3],[3,3],[5,3],[7,3],[9,3],[2,4],[4,4],[6,4],[8,4],[10,4],[1,5],[3,5],[5,5],[7,5],[9,5],[2,6],[4,6],[6,6],[8,6],[10,6],[1,7],[3,7],[5,7],[7,7],[9,7],[2,8],[4,8],[6,8],[8,8],[10,8],[1,9],[3,9],[5,9],[7,9],[9,9],[2,10],[4,10],[6,10],[8,10],[10,10]]
    possibilities=[1,2,3,4]
    player_grid = create_grid()
    computer_grid = create_grid()

    print("########## WELCOME TO BATTLESHIPS ##########")
    r.write("########## WELCOME TO BATTLESHIPS ##########")
    print("Rules:")
    r.write("Rules:")
    print("- The game is played on a 10x10 grid.")
    r.write("- The game is played on a 10x10 grid.")
    print("- Your fleet consists of 5 ships: Carrier (5 cells), Battleship (4 cells), Cruiser (3 cells), Submarine (3 cells), and Destroyer (2 cells).")
    r.write("- Your fleet consists of 5 ships: Carrier (5 cells), Battleship (4 cells), Cruiser (3 cells), Submarine (3 cells), and Destroyer (2 cells).")
    print("- Ships are placed vertically or horizontally on the grid.")
    r.write("- Ships are placed vertically or horizontally on the grid.")
    print("- The computer also has its own fleet.") 
    r.write("- The computer also has its own fleet.")
    print("- The first player to sink all of the opponent's ships wins.")
    r.write("- The first player to sink all of the opponent's ships wins.")
    print("\nLegend:")
    r.write("\nLegend:")
    print("- 'O' represents your ships.")
    r.write("- 'O' represents your ships.")
    print("- 'X' represents your ship_hits.")
    r.write("- 'X' represents your ship_hits.")
    print("- '*' represents missed shots.")
    r.write("- '*' represents missed shots.")
    print("- ' ' represents empty cells.")
    r.write("- ' ' represents empty cells.")
    print("\nLet's begin!\n")
    r.write("\nLet's begin!\n")


    print("Place your ships:")
    r.write("Place your ships:")
    print_grid(player_grid)
    for ship, length in [('Carrier', 5), ('Battleship', 4), ('Cruiser', 3), ('Submarine', 3), ('Destroyer', 2)]:
          while True:
            position = input(f"Enter the starting position (e.g., A1) for your {ship}: ")
            direction = input(f"Enter the direction (V for vertical, H for horizontal) for your {ship}: ")
            row, col = convert_input_to_coords(position)
            if can_place_ship(player_grid, [1] * length, row, col, direction):
                place_ship(player_grid, [1] * length, row, col, direction)
                break
            else:
                print("Invalid position! Try again.\n")
                r.write("Invalid position! Try again.\n")
    print_grid(player_grid)



    print("\nPlacing computer's ships...")
    r.write("\nPlacing computer's ships...")
    place_computer_ships(computer_grid)


    while True:

        print("\nYour turn!")
        r.write("\nYour turn!")
        print_grid(computer_grid)
        position = input("Enter the position to shoot at: ")
        row, col = convert_input_to_coords(position)
        hit = check_shot(computer_grid, row, col)
        print_grid(computer_grid)
        if hit:
            print("Hit!")
            r.write("Hit!")
            if check_game_over(computer_grid):
                print("Congratulations! You sunk all of the computer's ships. You win!")
                r.write("Congratulations! You sunk all of the computer's ships. You win!")
                break
        else:
            print("Missed!")
            r.write("Missed!")


        print("\nComputer's turn!")
        r.write("\nComputer's turn!")
        ship_hits,possibilties= computer_turn(player_grid,ship_hits,array,possibilities)


  play_game()
f.close()

