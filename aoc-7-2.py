def seconds(ch):
  return ord(ch) - 4

def nothingBlocks(A, rules):
  for rule in rules:
      if rule[1] == A:
          return False
  return True

with open("aoc-7-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]
alphabet = set({})
rules = []

for rule in content:
  rules.append((rule[5], rule[36]))
  alphabet.add(rule[5])
  alphabet.add(rule[36])

alphabet = list(alphabet)
alphabet.sort()

workers = [(0, ''), (0, ''), (0, ''), (0, ''), (0, '')]
alpha2 = alphabet[:]

seconds_past = 0
while len(rules) > 0 or len(alpha2) > 0:
  for i in range(len(workers)):
    if workers[i][0] == 0:
      if workers[i][1] != '':
        try:
          alpha2.remove(workers[i][1])
        except:
          pass
        j = 0
        while j < len(rules):
            if rules[j][0] == workers[i][1]:
              rules = rules[:j] + rules[j + 1:]
            else:
              j = j + 1
      for A in alphabet[:]:
        if nothingBlocks(A, rules):
          workers[i] = (seconds(A), A)
          alphabet.remove(A)
          break
  print("second: {}, {}".format(seconds_past, workers))
  for i in range(len(workers)):
    if workers[i][0] != 0:
      workers[i] = (workers[i][0] - 1, workers[i][1])
  seconds_past = seconds_past + 1

print(seconds_past - 1)
print(alphabet)
