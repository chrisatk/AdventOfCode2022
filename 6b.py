with open('6input.txt','r') as f:
  for ln in f:
    ln = ln.strip()

    for i in range(14,len(ln)):
      block = ln[i-14:i]
      match = 0
      for c in block:
        if (block.count(c) > 1):
          match = 1
      if (match == 0):
        print(block + " after "+ str(i))
        break
  
# Done reading file
