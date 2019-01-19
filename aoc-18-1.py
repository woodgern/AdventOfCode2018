from copy import deepcopy

def isTree(c):
  return 1 if c == '|' else 0

def isLumberyard(c):
  return 1 if c == '#' else 0

with open("aoc-18-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

grid = [['' for y in range(50)] for x in range(50)]

y = 0
for line in content:
  x = 0
  for c in line:
    grid[x][y] = c
    x += 1
  y += 1

for minutes in range(1, 11):
  old_grid = deepcopy(grid)
  for y in range(50):
    for x in range(50):
      if old_grid[x][y] == '.':
        adjacent_trees = 0
        if x > 0:
          adjacent_trees += isTree(old_grid[x - 1][y])
        if x < 49:
          adjacent_trees += isTree(old_grid[x + 1][y])
        if y > 0:
          adjacent_trees += isTree(old_grid[x][y - 1])
        if y < 49:
          adjacent_trees += isTree(old_grid[x][y + 1])
        if x > 0 and y > 0:
          adjacent_trees += isTree(old_grid[x - 1][y - 1])
        if x > 0 and y < 49:
          adjacent_trees += isTree(old_grid[x - 1][y + 1])
        if x < 49 and y > 0:
          adjacent_trees += isTree(old_grid[x + 1][y - 1])
        if x < 49 and y < 49:
          adjacent_trees += isTree(old_grid[x + 1][y + 1])
        if adjacent_trees >= 3:
          grid[x][y] = '|'
      elif old_grid[x][y] == '|':
        adjacent_lumberyards = 0
        if x > 0:
          adjacent_lumberyards += isLumberyard(old_grid[x - 1][y])
        if x < 49:
          adjacent_lumberyards += isLumberyard(old_grid[x + 1][y])
        if y > 0:
          adjacent_lumberyards += isLumberyard(old_grid[x][y - 1])
        if y < 49:
          adjacent_lumberyards += isLumberyard(old_grid[x][y + 1])
        if x > 0 and y > 0:
          adjacent_lumberyards += isLumberyard(old_grid[x - 1][y - 1])
        if x > 0 and y < 49:
          adjacent_lumberyards += isLumberyard(old_grid[x - 1][y + 1])
        if x < 49 and y > 0:
          adjacent_lumberyards += isLumberyard(old_grid[x + 1][y - 1])
        if x < 49 and y < 49:
          adjacent_lumberyards += isLumberyard(old_grid[x + 1][y + 1])
        if adjacent_lumberyards >= 3:
          grid[x][y] = '#'
      elif old_grid[x][y] == '#':
        adjacent_trees = 0
        if x > 0:
          adjacent_trees += isTree(old_grid[x - 1][y])
        if x < 49:
          adjacent_trees += isTree(old_grid[x + 1][y])
        if y > 0:
          adjacent_trees += isTree(old_grid[x][y - 1])
        if y < 49:
          adjacent_trees += isTree(old_grid[x][y + 1])
        if x > 0 and y > 0:
          adjacent_trees += isTree(old_grid[x - 1][y - 1])
        if x > 0 and y < 49:
          adjacent_trees += isTree(old_grid[x - 1][y + 1])
        if x < 49 and y > 0:
          adjacent_trees += isTree(old_grid[x + 1][y - 1])
        if x < 49 and y < 49:
          adjacent_trees += isTree(old_grid[x + 1][y + 1])

        adjacent_lumberyards = 0
        if x > 0:
          adjacent_lumberyards += isLumberyard(old_grid[x - 1][y])
        if x < 49:
          adjacent_lumberyards += isLumberyard(old_grid[x + 1][y])
        if y > 0:
          adjacent_lumberyards += isLumberyard(old_grid[x][y - 1])
        if y < 49:
          adjacent_lumberyards += isLumberyard(old_grid[x][y + 1])
        if x > 0 and y > 0:
          adjacent_lumberyards += isLumberyard(old_grid[x - 1][y - 1])
        if x > 0 and y < 49:
          adjacent_lumberyards += isLumberyard(old_grid[x - 1][y + 1])
        if x < 49 and y > 0:
          adjacent_lumberyards += isLumberyard(old_grid[x + 1][y - 1])
        if x < 49 and y < 49:
          adjacent_lumberyards += isLumberyard(old_grid[x + 1][y + 1])

        if not (adjacent_lumberyards >= 1 and adjacent_trees >= 1):
          grid[x][y] = '.'

total_trees = 0
total_lumberyards = 0
for y in range(50):
  for x in range(50):
    if grid[x][y] == '|':
      total_trees += 1
    if grid[x][y] == '#':
      total_lumberyards += 1

print(total_lumberyards * total_trees)
