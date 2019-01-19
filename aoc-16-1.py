def addr(registers, A, B, C):
  r = registers.copy()
  r[C] = r[A] + r[B]
  return r

def addi(registers, A, B, C):
  r = registers.copy()
  r[C] = r[A] + B
  return r

def mulr(registers, A, B, C):
  r = registers.copy()
  r[C] = r[A] * r[B]
  return r

def muli(registers, A, B, C):
  r = registers.copy()
  r[C] = r[A] * B
  return r

def banr(registers, A, B, C):
  r = registers.copy()
  r[C] = r[A] & r[B]
  return r

def bani(registers, A, B, C):
  r = registers.copy()
  r[C] = r[A] & B
  return r

def borr(registers, A, B, C):
  r = registers.copy()
  r[C] = r[A] | r[B]
  return r

def bori(registers, A, B, C):
  r = registers.copy()
  r[C] = r[A] | B
  return r

def setr(registers, A, B, C):
  r = registers.copy()
  r[C] = r[A]
  return r

def seti(registers, A, B, C):
  r = registers.copy()
  r[C] = A
  return r

def gtir(registers, A, B, C):
  r = registers.copy()
  r[C] = 1 if A > r[B] else 0
  return r

def gtri(registers, A, B, C):
  r = registers.copy()
  r[C] = 1 if r[A] > B else 0
  return r

def gtrr(registers, A, B, C):
  r = registers.copy()
  r[C] = 1 if r[A] > r[B] else 0
  return r

def eqir(registers, A, B, C):
  r = registers.copy()
  r[C] = 1 if A == r[B] else 0
  return r

def eqri(registers, A, B, C):
  r = registers.copy()
  r[C] = 1 if r[A] == B else 0
  return r

def eqrr(registers, A, B, C):
  r = registers.copy()
  r[C] = 1 if r[A] == r[B] else 0
  return r

with open("aoc-16-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtri, gtir, gtrr, eqri, eqir, eqrr]
cases = []
current_case = [None, None, None]
pointer = 0
for c in content:
  if pointer == 0:
    c = c.split(':')
    registers_string = c[1].strip(' ').strip('[').strip(']')
    registers = registers_string.split(', ')
    registers = list(map(lambda x: int(x), registers))
    current_case[0] = registers
  elif pointer == 1:
    inputs = list(map(lambda x: int(x), c.split(' ')))
    current_case[1] = inputs
  elif pointer == 2:
    c = c.split(':')
    registers_string = c[1].strip(' ').strip('[').strip(']')
    registers = registers_string.split(', ')
    registers = list(map(lambda x: int(x), registers))
    current_case[2] = registers
  else:
    cases.append(current_case)
    current_case = [None, None, None]

  pointer = (pointer + 1) % 4
cases.append(current_case)

count = 0
for case in cases:
  local_count = 0
  for op in ops:
    if op(case[0], case[1][1], case[1][2], case[1][3]) == case[2]:
      local_count += 1
  if local_count >= 3:
    count += 1

print(count)

