with open("aoc-1-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

def doThing(content):
	total = 0
	seen = [0]
	while True:
		for delta in content:
			total = total + int(delta)
			if total in seen:
				return total
			else:
				seen.append(total)

print(doThing(content))
