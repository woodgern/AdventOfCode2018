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

def final_form(op_map):
  for i in range(16):
    if len(op_map[i]) > 1:
      return False
  return True

with open("aoc-16-2.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtri, gtir, gtrr, eqri, eqir, eqrr]
cases = []
instructions = []
current_case = [None, None, None]
pointer = 0
stage2 = False
for c in content:
  if not stage2:
    if pointer == 0:
      if len(c) == 0:
        stage2 = True
        continue
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
  else:
    if len(c) != 0:
      inputs = list(map(lambda x: int(x), c.split(' ')))
      instructions.append(inputs)

op_map = {}
for i in range(16):
  op_map[i] = set([])

for case in cases:
  temp_op_map = {}
  for i in range(16):
    temp_op_map[i] = False

  for i in range(len(ops)):
    if ops[i](case[0], case[1][1], case[1][2], case[1][3]) == case[2]:
      temp_op_map[i] = True

  for i in range(16):
    if not temp_op_map[i]:
      op_map[i].add(case[1][0])

a = set(range(16))
for i in range(16):
  op_map[i] = a.difference(op_map[i])

while not final_form(op_map):
  for i in range(16):
    if len(op_map[i]) == 1:
      for j in range(16):
        if i != j:
          op_map[j] = op_map[j].difference(op_map[i])

for i in range(16):
  op_map[i] = list(op_map[i])[0]

machine = {}
for i in range(16):
  machine[op_map[i]] = i

registers = [0, 0, 0, 0]
for instruction in instructions:
  registers = ops[machine[instruction[0]]](registers, instruction[1], instruction[2], instruction[3])

print(registers)
