import random

def printGrid(grid, x_ext, y_ext):
  for y in range(y_ext):
    for x in range(x_ext):
      print(grid[x][y], end='')
    print()

with open("aoc-17-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

coords = []

x_ext = 0
y_ext = 0
for line in content:
  xandy = line.split(', ')
  if xandy[0][0] == 'x':
    x = int(xandy[0].split('=')[1])
    if x > x_ext:
      x_ext = x
    ys = xandy[1].split('=')[1]
    y1 = int(ys.split('..')[0])
    y2 = int(ys.split('..')[1])
    if y2 > y_ext:
      y_ext = y2
    for y in range(y1, y2 + 1):
      coords.append((x, y))
  elif xandy[0][0] == 'y':
    y = int(xandy[0].split('=')[1])
    if y > y_ext:
      y_ext = y
    xs = xandy[1].split('=')[1]
    x1 = int(xs.split('..')[0])
    x2 = int(xs.split('..')[1])
    if x2 > x_ext:
      x_ext = x2
    for x in range(x1, x2 + 1):
      coords.append((x, y))

x_ext += 4
y_ext += 1
grid = [['.' for y in range(y_ext)] for x in range(x_ext)]
grid[500][0] = '+'
for coord in coords:
  grid[coord[0]][coord[1]] = '#'

count = 0
oldSettled = 0
totalSettled = 0
allSettled = False
while not allSettled:
  settled = False
  h = (500, 1)
  direction = 'd'
  wall_hits = 0
  while not settled:
    if direction == 'd':
      if h[1] + 1 >= y_ext:
        grid[h[0]][h[1]] = '|'
        break
      elif grid[h[0]][h[1] + 1] == '.' or grid[h[0]][h[1] + 1] == '|':
        grid[h[0]][h[1]] = '|'
        grid[h[0]][h[1] + 1] = '~'
        h = (h[0], h[1] + 1)
      elif grid[h[0]][h[1] + 1] == '#' or grid[h[0]][h[1] + 1] == '~':
        choice = random.random()
        if choice < 0.5:
          direction = 'l'
        else:
          direction = 'r'
    elif direction == 'r':
      if h[0] + 1 >= x_ext:
        grid[h[0]][h[1]] = '|'
        settled = True
      if grid[h[0]][h[1] + 1] == '.' or grid[h[0]][h[1] + 1] == '|':
        direction = 'd'
        wall_hits = 0
      elif grid[h[0] + 1][h[1]] == '.' or grid[h[0] + 1][h[1]] == '|':
        grid[h[0]][h[1]] = '|'
        grid[h[0] + 1][h[1]] = '~'
        h = (h[0] + 1, h[1])
      elif grid[h[0] + 1][h[1]] == '#' or grid[h[0] + 1][h[1]] == '~':
        if wall_hits == 0:
          direction = 'l'
          wall_hits += 1
        else:
          settled = True
          totalSettled += 1
    elif direction == 'l':
      if h[0] - 1 <= 0:
        grid[h[0]][h[1]] = '|'
        settled = True
      if grid[h[0]][h[1] + 1] == '.' or grid[h[0]][h[1] + 1] == '|':
        direction = 'd'
        wall_hits = 0
      elif grid[h[0] - 1][h[1]] == '.' or grid[h[0] - 1][h[1]] == '|':
        grid[h[0]][h[1]] = '|'
        grid[h[0] - 1][h[1]] = '~'
        h = (h[0] - 1, h[1])
      elif grid[h[0] - 1][h[1]] == '#' or grid[h[0] - 1][h[1]] == '~':
        if wall_hits == 0:
          direction = 'r'
          wall_hits += 1
        else:
          settled = True
          totalSettled += 1

  if oldSettled == totalSettled:
    count += 1
  oldSettled = totalSettled

  if count >= 15000:
    break

for y in range(y_ext - 1):
  for x in range(x_ext - 1):
    if (grid[x][y] == '.' or grid[x][y] == '|')  and grid[x - 1][y] == '~' and grid[x][y + 1] == '~':
      grid[x][y] = '~'

water_count = 0
for y in range(y_ext):
  for x in range(x_ext):
    if grid[x][y] == '~' or grid[x][y] == '|':
      water_count += 1

printGrid(grid, x_ext, y_ext)
print(water_count)



