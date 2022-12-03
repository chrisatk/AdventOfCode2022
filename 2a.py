def play(myPlay):
  points = 0
  if (myPlay[2] == "X" and myPlay[0] == "C") or (myPlay[2] == "Y" and myPlay[0] == "A") or (myPlay[2] == "Z" and myPlay[0] == "B"):
    # I win
    points = 6
  elif ord(myPlay[2]) == (ord(myPlay[0])+23):
    # Draw
    points = 3
  # Add points for the shape I chose
  if myPlay[2] == "X":
    points = points + 1
  elif myPlay[2] == "Y":
    points = points + 2
  else:
    points = points + 3
  return points
    
score = 0
with open('2input.txt','r') as f:
  for ln in f:
    ln = ln.strip()
    score = score + play(ln)
  
# Done reading file
print (score)