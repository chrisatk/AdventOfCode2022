def check(elf1,elf2):
  ranges = elf1.split("-")
  compareTo = elf2.split("-")
  if int(compareTo[0]) >= int(ranges[0]) and int(compareTo[1]) <= int(ranges[1]):
    return 1
  else:
    return 0

count = 0
with open('4input.txt','r') as f:
  for ln in f:
    ln = ln.strip()
    elf = ln.split(",")
    newCount = 0
    #check one way
    newCount = check(elf[0],elf[1])
    if newCount == 0:
      #check reverse
      newCount = check(elf[1],elf[0])
    count = count + newCount
# Done reading file
print(count)