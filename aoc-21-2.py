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

with open("aoc-21-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

opcode_map = {
	"addr": addr,
	"addi": addi,
	"mulr": mulr,
	"muli": muli,
	"banr": banr,
	"bani": bani,
	"borr": borr,
	"bori": bori,
	"setr": setr,
	"seti": seti,
	"gtri": gtri,
	"gtir": gtir,
	"gtrr": gtrr,
	"eqir": eqir,
	"eqri": eqri,
	"eqrr": eqrr
}

instructions = []

for line in content:
	s = line.split(' ')
	if s[0] == '#ip':
		instructions.append((s[0], int(s[1])))
	else:
		instructions.append((s[0], int(s[1]), int(s[2]), int(s[3])))

ip = 0
ipr = instructions[0][1]
instructions = instructions[1:]

seen = set({})
count = 0
prev = 0
registers = [0, 0, 0, 0, 0, 0]
while ip < len(instructions) and ip >= 0:
    instruct = instructions[ip]
    registers[ipr] = ip
    registers = opcode_map[instruct[0]](registers, instruct[1], instruct[2], instruct[3])
    if instruct[0] == 'eqrr':
      if registers[5] in seen:
        break
      seen.add(registers[5])
      prev = registers[5]

    # print("{} {} {} {}".format(instruct[0], instruct[1], instruct[2], instruct[3]))
    # print("Registers: {}".format(registers))
    # print()
    count += 1
    ip = registers[ipr]
    ip += 1
print(prev)
print(len(seen))