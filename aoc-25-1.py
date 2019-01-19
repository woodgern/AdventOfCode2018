def distance(v1, v2):
  return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1]) + abs(v1[2] - v2[2]) + abs(v1[3] - v2[3])

def is_combinable(l1, l2):
  for item in l1:
    for item2 in l2:
      if distance(item, item2) <= 3 and item != item2:
        return True
  return False

with open("aoc-25-1.txt") as f:
  content = f.readlines()

content = [x.strip() for x in content]

conts = []
for line in content:
  nums = line.split(',')
  conts.append([(int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3]))])

old_length = -1

while len(conts) != old_length: 
  old_length = len(conts)
  new_conts = []
  i = 0
  while i < len(conts):
    cur_cont = conts[i]
    j = i + 1
    while j < len(conts):
      if i != j and is_combinable(conts[i], conts[j]):
        cur_cont.extend(conts[j])
        del conts[j]
      j += 1
    new_conts.append(cur_cont)
    i += 1
  conts = new_conts

print(len(conts))



