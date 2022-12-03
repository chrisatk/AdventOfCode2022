elf_list = []

with open('input.txt','r') as f:
  elf = 0
  for ln in f:
    ln = ln.strip()
    if ln == "":
      # Start a new elf
      elf_list.append(elf)
      elf = 0
    else: 
      # Add to current elf
      elf = elf + int(ln)
      

# Done reading file
elf_list.sort(reverse=True)
print (elf_list[0])