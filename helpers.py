def drawboard(spots):
  drawboard = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
                 f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"f"|{spots[7]}|{spots[8]}|{spots[9]}|")

  print(drawboard)

def check_turn(turn):
  if turn % 2 == 0:
    return 'O'
  else:
    return 'X'
  
  
def win_check(spots):

#Horizontal Wins

  if   (spots[1] == spots[2] == spots[3]) \
    or (spots[4] == spots[5] == spots[6]) \
    or (spots[7] == spots[8] == spots[9]):
    return True

#Vertical Wins

  elif   (spots[1] == spots[4] == spots[7]) \
    or (spots[2] == spots[5] == spots[8]) \
    or (spots[3] == spots[6] == spots[9]):
    return True

#Diagonal Wins

  elif (spots[1] == spots[5] == spots[9]) \
    or (spots[3] == spots[5] == spots[7]):
    return True
  
  else: return False
