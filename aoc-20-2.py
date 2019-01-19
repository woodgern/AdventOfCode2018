from itertools import product
import sys

class Room:
  def __init__(self):
    self.up = False
    self.down = False
    self.left = False
    self.right = False
    self.distance = 10001

def splitRegex(regex):
  blocks = []
  braceDepth = 0
  blockStart = 0
  for i in range(len(regex)):
    if regex[i] == '(':
      braceDepth += 1
    elif regex[i] == ')':
      braceDepth -= 1
    elif regex[i] == '|' and braceDepth == 0:
      blocks.append(regex[blockStart:i])
      blockStart = i + 1

  if regex[blockStart:] != '':
    blocks.append(regex[blockStart:])

  return blocks

def blockify(regex):
  blocks = []
  braceDepth = 0
  blockStart = 0
  for i in range(len(regex)):
    if regex[i] == '(' and braceDepth == 0:
      if regex[blockStart:i] != '':
        blocks.append(regex[blockStart:i])
      braceDepth += 1
      blockStart = i
    elif regex[i] == '(':
      braceDepth += 1
    elif regex[i] == ')' and braceDepth != 1:
      braceDepth -= 1
    elif regex[i] == ')':
      braceDepth -= 1
      if regex[blockStart:i] != '':
        blocks.append(regex[blockStart:i + 1])
      blockStart = i + 1

  if regex[blockStart:] != '':
    blocks.append(regex[blockStart:])

  return blocks

def generatePaths(regex):
  blocks = blockify(regex)

  paths = []
  blockPaths = []
  if len(blocks) == 1:
    regex = blocks[0]
    if regex[0] == '(':
      regex = regex[1:-1]
      b = splitRegex(regex)
      for block in b:
        paths.extend(generatePaths(block))
      return paths
    else:
      return [regex]
  else:
    for block in blocks:
      blockPaths.append(generatePaths(block))

  paths = product(*blockPaths)
  paths = ["".join(path) for path in paths]

  return paths


def floodFill(grid, x, y, distance):
  grid[x][y].distance = distance

  if grid[x][y].up:
    if grid[x][y - 1].distance > grid[x][y].distance + 1:
      floodFill(grid, x, y - 1, grid[x][y].distance + 1)
  if grid[x][y].down:
    if grid[x][y + 1].distance > grid[x][y].distance + 1:
      floodFill(grid, x, y + 1, grid[x][y].distance + 1)
  if grid[x][y].right:
    if grid[x + 1][y].distance > grid[x][y].distance + 1:
      floodFill(grid, x + 1, y, grid[x][y].distance + 1)
  if grid[x][y].left:
    if grid[x - 1][y].distance > grid[x][y].distance + 1:
      floodFill(grid, x - 1, y, grid[x][y].distance + 1)




sys.setrecursionlimit(10000)

with open("aoc-20-1.txt") as f:
    content = f.readlines()

regex = [x.strip() for x in content][0][1:-1]

paths = generatePaths(regex)

grid = [[Room() for y in range(100)] for x in range(100)]

for path in paths:
  x = 50
  y = 47
  for d in path:
    if d == 'N':
      grid[x][y].up = True
      y -= 1
    elif d == 'S':
      grid[x][y].down = True
      y += 1
    elif d == 'E':
      grid[x][y].right = True
      x += 1
    elif d == 'W':
      grid[x][y].left = True
      x -= 1

floodFill(grid, 50, 47, 0)

count = 0
for y in range(100):
  for x in range(100):
    if grid[x][y].distance >= 1000:
      count += 1
print(count)



