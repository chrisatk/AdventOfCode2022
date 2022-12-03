def findRepeats(sidea,sideb):
  repeat = ""
  for ca in sidea:
    for cb in sideb:
      if ca == cb:
        repeat = ca
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

with open('3input.txt','r') as f:
  for ln in f:
    ln = ln.strip()

    length = int(len(ln))
    midpoint = int(length/2)
    sidea = ln[0:midpoint]
    sideb = ln[midpoint:length]

    myRepeat = findRepeats(sidea,sideb)
    priority = priority + scoreRepeat(myRepeat)      
  
# Done reading file
print (priority)
