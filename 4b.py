def check(elf1,elf2):
  ranges = elf1.split("-")
  compareTo = elf2.split("-")
  hit = 0
  if int(compareTo[0]) in range(int(ranges[0]),int(ranges[1])+1):
    hit = 1
  if int(compareTo[1]) in range(int(ranges[0]),int(ranges[1])+1):
    hit = 1
  return hit

count = 0
with open('4input.txt','r') as f:
  for ln in f:
    ln = ln.strip()
    elf = ln.split(",")
    newCount = 0
    newCount = check(elf[0],elf[1])
    if newCount == 0:
      newCount = check(elf[1],elf[0])
    count = count + newCount
# Done reading file
print(count)
