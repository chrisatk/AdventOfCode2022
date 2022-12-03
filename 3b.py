def findRepeats(sidea,sideb):
  repeat = ""
  for ca in sidea:
    for cb in sideb:
      if ca == cb:
        repeat = repeat + ca
#        print("comparing "+ ca + " and "+ cb + " MATCH")
#      else :
#        print("comparing "+ ca + " and "+ cb)
  return repeat

def scoreRepeat(repeat):
  if repeat.islower():
    return ord(repeat)-96
  else:
    return ord(repeat)-38
          
priority = 0
sidea = ""
sideb = ""
repeat = ""

lineCounter = 0
with open('3input.txt','r') as f:
  for ln in f:
    ln = ln.strip()

    if lineCounter % 3 == 0: # new group
      repeat = "" # clear repeat
      sideb = "" # clear sideb
      sidea = ln # set sidea
    elif lineCounter % 3 == 1: # second in a group
      sideb = ln
      repeat = findRepeats(sidea,sideb)
#      print (repeat+ " repeats in line 1 & 2")
    elif lineCounter % 3 == 2: # third in a group
      sidea = sideb
      sideb = ln
      repeat = findRepeats(repeat,findRepeats(sidea,sideb))
#      print (repeat+ " repeats in line 2 & 3")
      priority = priority + scoreRepeat(repeat[0])      
      
    lineCounter = lineCounter + 1
  
# Done reading file
print (priority)
