def new_edge(plants, old_edge):
  count = 0
  for plant in plants:
    if plant == '.':
      count += 1
    else:
      break
  return old_edge + (count - 4)

def pad(l):
  string = ''.join(l)
  return list("...." + string.strip('.') + "....")

with open("aoc-12-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

plants = list(content[0].split(' ')[2])

rule_list = content[2:]
rules = {}

for rule_string in rule_list:
  rule_string_parts = rule_string.split(' => ')
  rules[rule_string_parts[0]] = rule_string_parts[1]


edge = 0
for generation in range(1, 21):
  edge = new_edge(plants, edge)
  plants = pad(plants)
  new_plants = plants[:]

  for i in range(2, len(plants) - 2):
    new_plants[i] = rules[''.join(plants[i - 2:i + 3])]
  plants = new_plants

answer = 0
for i in range(len(plants)):
  if plants[i] == "#":
    answer += (edge + i)

print(answer)
