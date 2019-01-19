def printGrid(grid):
  for y in range(len(grid[0])):
    for x in range(len(grid)):
      print(grid[x][y], end='')
    print()

depth = 3066
tx = 13
ty = 726

grid = [[-1 for y in range(ty + 1)] for x in range(tx + 1)]

grid[0][0] = 0

for y in range(ty + 1):
  for x in range(tx + 1):
    if x == 0 and y == 0:
      continue
    if x == 0:
      grid[x][y] = (y * 48271)
    elif y == 0:
      grid[x][y] = (x * 16807)
    else:
      grid[x][y] = grid[x - 1][y] * grid[x][y - 1]

    grid[x][y] =  (grid[x][y] + depth) % 20183

grid[tx][ty] = depth

risk = 0
for y in range(ty + 1):
  for x in range(tx + 1):
    risk += (grid[x][y] % 3)
print(risk)


