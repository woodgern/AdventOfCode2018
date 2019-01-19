with open("aoc-1-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

total = 0
for delta in content:
	total = total + int(delta)

print(total)
