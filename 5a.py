import re
stacks = {}
stacks['stack1'] = ['F','C','P','G','Q','R']
stacks['stack2'] = ['W','T','C','P']
stacks['stack3'] = ['B','H','P','M','C']
stacks['stack4'] = ['L','T','Q','S','M','P','R']
stacks['stack5'] = ['P','H','J','Z','V','G','N']
stacks['stack6'] = ['D','P','J']
stacks['stack7'] = ['L','G','P','Z','F','J','T','R']
stacks['stack8'] = ['N','L','H','C','F','P','T','J']
stacks['stack9'] = ['G','V','Z','Q','H','T','C','W']

with open('5input.txt','r') as f:
  for ln in f:
    ln = ln.strip()
    # Using re function for multiple splits 
    # ref: https://datagy.io/python-split-string-multiple-delimiters/
    instructions = re.split(r' from | to ', ln[5:len(ln)])

    for i in range (int(instructions[0])):
      stacks['stack'+instructions[2]].append(stacks['stack'+instructions[1]].pop())
  
# Done reading file
for i in range(1,10):
  print(stacks['stack'+str(i)].pop())