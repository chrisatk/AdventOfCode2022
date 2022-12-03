def play(myPlay):  
  outcome = myPlay[2]
  otherPlayer = myPlay[0]
  match outcome:
    case 'X': #Loss
      match otherPlayer:
        case 'A': # They played Rock, I played Scissor
          return 3
        case 'B': # They played Paper, I played Rock
          return 1
        case 'C': # They played Scissor, I played Paper
          return 2
    case 'Y': #Draw
      match otherPlayer:
        case 'A': # They played Rock
          return 4
        case 'B': # They played Paper
          return 5
        case 'C': # They played Scissor
          return 6
    case 'Z': #Win
      match otherPlayer:
        case 'A': # They played Rock, I played Paper
          return 8
        case 'B': # They played Paper, I played Scissor
          return 9
        case 'C': # They played Scissor, I played Rock
          return 7
    
score = 0
with open('2input.txt','r') as f:
  for ln in f:
    ln = ln.strip()
    score = score + play(ln)
  
# Done reading file
print (score)