import sys

class Region:
  def __init__(self):
    self.type = '.'
    self.map = {
      0: 10000,
      1: 10000,
      2: 10000
    }
def printGrid(grid):
  for y in range(len(grid[0])):
    for x in range(len(grid)):
      print(grid[x][y].type, end='')
    print()

# 0 is netiher, 1 is torch, 2 is climbing tool
def jivesWith(item, t):
  if t == '.' and (item == 1 or item == 2):
    return True
  if t == '=' and (item == 0 or item == 2):
    return True
  if t == '|' and (item == 0 or item == 1):
    return True
  return False

def other(item, t):
  if t == '.' and item == 1:
    return 2
  if t == '.' and item == 2:
    return 1
  if t == '=' and item == 0:
    return 2
  if t == '=' and item == 2:
    return 0
  if t == '|' and item == 0:
    return 1
  if t == '|' and item == 1:
    return 0

def flood_fill(grid, item, x, y, value):
  grid[x][y].map[item] = value

  if x > 0:
    if jivesWith(item, grid[x - 1][y].type):
      if value + 1 < grid[x - 1][y].map[item]:
        flood_fill(grid, item, x - 1, y, value + 1)
    if jivesWith(other(item, grid[x][y].type), grid[x - 1][y].type):
      if value + 8 < grid[x - 1][y].map[other(item, grid[x][y].type)]:
        flood_fill(grid, other(item, grid[x][y].type), x - 1, y, value + 8)
  if y > 0:
    if jivesWith(item, grid[x][y - 1].type):
      if value + 1 < grid[x][y - 1].map[item]:
        flood_fill(grid, item, x, y - 1, value + 1)
    if jivesWith(other(item, grid[x][y].type), grid[x][y - 1].type):
      if value + 8 < grid[x][y - 1].map[other(item, grid[x][y].type)]:
        flood_fill(grid, other(item, grid[x][y].type), x, y - 1, value + 8)
  if x + 1 < len(grid):
    if jivesWith(item, grid[x + 1][y].type):
      if value + 1 < grid[x + 1][y].map[item]:
        flood_fill(grid, item, x + 1, y, value + 1)
    if jivesWith(other(item, grid[x][y].type), grid[x + 1][y].type):
      if value + 8 < grid[x + 1][y].map[other(item, grid[x][y].type)]:
        flood_fill(grid, other(item, grid[x][y].type), x + 1, y, value + 8)
  if y + 1 < len(grid[0]):
    if jivesWith(item, grid[x][y + 1].type):
      if value + 1 < grid[x][y + 1].map[item]:
        flood_fill(grid, item, x, y + 1, value + 1)
    if jivesWith(other(item, grid[x][y].type), grid[x][y + 1].type):
      if value + 8 < grid[x][y + 1].map[other(item, grid[x][y].type)]:
        flood_fill(grid, other(item, grid[x][y].type), x, y + 1, value + 8)


sys.setrecursionlimit(100000)

depth = 3066
tx = 13
ty = 726

grid = [[Region() for y in range(ty + 30)] for x in range(tx + 30)]

grid[0][0].type = 0

for y in range(ty + 30):
  for x in range(tx + 30):
    if x == 0 and y == 0:
      continue

    if x == tx and y == ty:
      grid[tx][ty].type = depth
      continue
    if x == 0:
      grid[x][y].type = (y * 48271)
    elif y == 0:
      grid[x][y].type = (x * 16807)
    else:
      grid[x][y].type = grid[x - 1][y].type * grid[x][y - 1].type

    grid[x][y].type =  (grid[x][y].type + depth) % 20183


for y in range(ty + 30):
  for x in range(tx + 30):
    if grid[x][y].type % 3 == 0:
      grid[x][y].type = '.'
    elif grid[x][y].type % 3 == 1:
      grid[x][y].type = '='
    elif grid[x][y].type % 3 == 2:
      grid[x][y].type = '|'

flood_fill(grid, 1, 0, 0, 0)
target_reached = grid[tx][ty].map
print(min(target_reached[0] + 7, target_reached[1], target_reached[2] + 7))


