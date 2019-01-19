with open("aoc-3-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

grid = [[0 for x in range(1000)] for y in range(1000)] 

previous = []
for claim in content:
	claim_array = claim.split(" ")
	claim_location = claim_array[2].split(',')
	x = int(claim_location[0])
	y = int(claim_location[1].strip(':'))
	claim_size = claim_array[3].split('x')
	width = int(claim_size[0])
	height = int(claim_size[1])

	for i in range(width):
		for j in range(height):
			grid[i + x][j + y] = grid[i + x][j + y] + 1

count = 0
for i in range(1000):
	for j in range(1000):
		if grid[i][j] >= 2:
			count = count + 1

print(count)