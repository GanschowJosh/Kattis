from sys import stdin

RAM = [0] * 1000
for i, line in enumerate(stdin):
  if line.strip():
    RAM[i] = int(line)

registers = [0] * 10


def process(idx):
  a = RAM[idx] // 100
  b = (RAM[idx] // 10) % 10
  c = RAM[idx] % 10

  if a == 1:
    return -1
  elif a == 2:
    registers[b] = c
  elif a == 3:
    registers[b] = (registers[b] + c) % 1000
  elif a == 4:
    registers[b] = (registers[b] * c) % 1000
  elif a == 5:
    registers[b] = registers[c]
  elif a == 6:
    registers[b] = (registers[b] + registers[c]) % 1000
  elif a == 7:
    registers[b] = (registers[b] * registers[c]) % 1000
  elif a == 8:
    registers[b] = RAM[registers[c]]
  elif a == 9:
    RAM[registers[c]] = registers[b]
  elif a == 0 and registers[c]:
    return registers[b]

  return (idx + 1) % 1000

pc = 0
count = 0
while True:
  count += 1
  pc = process(pc)
  if pc == -1:
    print(count)
    break
