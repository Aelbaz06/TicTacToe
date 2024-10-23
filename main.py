from helpers import drawboard, check_turn, win_check
import os, time
spots = {1: '1', 2 : '2', 3 : '3', 4 : '4',5 : '5', 
         6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
turn = 0
complete = False
while playing:
  # Reset the play section/area
  os.system('cls' if os.name == 'nt' else 'clear')
  drawboard(spots)
  print("Player " +str((turn % 2) +1) + " 's turn: Pick a spot or press q to quit.")
  # This gets input from player
  choice = input()
  if choice == 'q':
      playing = False

  # Check if input is a valid number
  if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:

    # Check if spot is taken
    if spots[int(choice)] in ['X', 'O']:
      print('Spot is taken, choose somewhere else that is open')
      time.sleep(1)
      spots[int(choice)] != check_turn(turn)
      turn -= 1

    else:
      #update the spots with X or O
      spots[int(choice)] = check_turn(turn)

      # Increment turn by 1
    turn += 1

if win_check(spots): playing, compete = False, True
if turn > 8: playing = False 


os.system('cls' if os.name == 'nt' else 'clear')
drawboard(spots)

if win_check(spots) == True: 
  if check_turn(turn) == 'X': 
    print("Player 1 Wins!")
  else: print("Player 2 Wins!")
else: 
  #tie game
  print("No Winner!")

print("Thanks for Playing")
