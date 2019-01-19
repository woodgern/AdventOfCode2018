with open("aoc-2-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

threes = 0
twos = 0
for id in content:
	letters = [0] * 26
	for c in id:
		letters[ord(c) - 97] = letters[ord(c) - 97] + 1
	if 2 in letters:
		twos = twos + 1
	if 3 in letters:
		threes = threes + 1


print(threes * twos)
