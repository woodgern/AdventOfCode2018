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

answer_string = ''
while len(rules) > 0:
  for A in alphabet[:]:
      cont = False
      for rule in rules:
          if rule[1] == A:
              cont = True
              break

      if cont:
          continue

      answer_string = answer_string + A
      alphabet.remove(A)
      i = 0
      while i < len(rules):
          if rules[i][0] == A:
            rules = rules[:i] + rules[i + 1:]
          else:
            i = i + 1
      break
        
            
print(answer_string)
print(alphabet)
