import copy
import sys

def doTheSort(carts):
  s1 = sorted(carts, key=lambda cart: cart[1][0])
  return sorted(s1, key=lambda cart: cart[1][1])
def printGrid(grid):
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      print(grid[y][x], end = '')
    print('')

with open("aoc-13-1.txt") as f:
    content = f.readlines()

content = [x for x in content]

og_grid = [['' for y in range(155)] for x in range(155)]
carts = []

line_count = 0
for line in content:
  column = 0
  for char in line:
    if char == '^':
      carts.append([1, (column, line_count), 'l'])
    elif char == '>':
      carts.append([2, (column, line_count), 'l'])
    elif char == 'v':
      carts.append([3, (column, line_count), 'l'])
    elif char == '<':
      carts.append([4, (column, line_count), 'l'])

    og_grid[column][line_count] = char
    column += 1
  line_count += 1

grid = copy.deepcopy(og_grid)

# for x in range(1, 154):
#   for y in range(1, 154):
#     if og_grid[x-1][y] != ' ' and og_grid[x+1][y] != ' ' and og_grid[x][y-1] != ' ' and og_grid[x][y+1] != ' ':
#       og_grid[x][y] = '+'
#     elif og_grid[x-1][y] != ' ' and og_grid[x+1][y] != ' ':
#       og_grid[x][y] = '-'
#     elif og_grid[x][y-1] != ' ' and og_grid[x][y+1] != ' ':
#       og_grid[x][y] = '|'
#     elif og_grid[x-1][y] != ' ' and og_grid[x][y-1] != ' ':
#       og_grid[x][y] = '/'
#     elif og_grid[x-1][y] != ' ' and og_grid[x][y+1] != ' ':
#       og_grid[x][y] = '\\'
#     elif og_grid[x+1][y] != ' ' and og_grid[x][y-1] != ' ':
#       og_grid[x][y] = '\\'
#     elif og_grid[x+1][y] != ' ' and og_grid[x][y+1] != ' ':
#       og_grid[x][y] = '/'


tick = 0
finished = False
while not finished:
  for cart in carts:
    if cart[0] == 1:
      grid[cart[1][0]][cart[1][1]] = og_grid[cart[1][0]][cart[1][1]]
      if grid[cart[1][0]][cart[1][1] - 1] == '/':
        cart[0] = 2
      elif grid[cart[1][0]][cart[1][1] - 1] == '\\':
        cart[0] = 4
      elif grid[cart[1][0]][cart[1][1] - 1] == '+':
        if cart[2] == 'l':
          cart[0] = 4
          cart[2] = 's'
        elif cart[2] == 's':
          cart[2] = 'r'
        elif cart[2] == 'r':
          cart[0] = 2
          cart[2] = 'l'
      elif grid[cart[1][0]][cart[1][1] - 1] == '.':
        grid[cart[1][0]][cart[1][1] - 1] = '&'
        print("{}, {}".format(cart[1][0], cart[1][1] - 1))
        finished = True
        break

      grid[cart[1][0]][cart[1][1] - 1] = '.'
      cart[1] = (cart[1][0], cart[1][1] - 1)
    elif cart[0] == 2:
      grid[cart[1][0]][cart[1][1]] = og_grid[cart[1][0]][cart[1][1]]
      if grid[cart[1][0] + 1][cart[1][1]] == '/':
        cart[0] = 1
      elif grid[cart[1][0] + 1][cart[1][1]] == '\\':
        cart[0] = 3
      elif grid[cart[1][0] + 1][cart[1][1]] == '+':
        if cart[2] == 'l':
          cart[0] = 1
          cart[2] = 's'
        elif cart[2] == 's':
          cart[2] = 'r'
        elif cart[2] == 'r':
          cart[0] = 3
          cart[2] = 'l'
      elif grid[cart[1][0] + 1][cart[1][1]] == '.':
        grid[cart[1][0] + 1][cart[1][1]] = '&'
        print("{}, {}".format(cart[1][0] + 1, cart[1][1]))
        finished = True
        break

      grid[cart[1][0] + 1][cart[1][1]] = '.'
      cart[1] = (cart[1][0] + 1, cart[1][1])
    elif cart[0] == 3:
      grid[cart[1][0]][cart[1][1]] = og_grid[cart[1][0]][cart[1][1]]
      if grid[cart[1][0]][cart[1][1] + 1] == '/':
        cart[0] = 4
      elif grid[cart[1][0]][cart[1][1] + 1] == '\\':
        cart[0] = 2
      elif grid[cart[1][0]][cart[1][1] + 1] == '+':
        if cart[2] == 'l':
          cart[0] = 2
          cart[2] = 's'
        elif cart[2] == 's':
          cart[2] = 'r'
        elif cart[2] == 'r':
          cart[0] = 4
          cart[2] = 'l'
      elif grid[cart[1][0]][cart[1][1] + 1] == '.':
        grid[cart[1][0]][cart[1][1] + 1] = '&'
        print("{}, {}".format(cart[1][0], cart[1][1] + 1))
        finished = True
        break

      grid[cart[1][0]][cart[1][1] + 1] = '.'
      cart[1] = (cart[1][0], cart[1][1] + 1)
    elif cart[0] == 4:
      grid[cart[1][0]][cart[1][1]] = og_grid[cart[1][0]][cart[1][1]]
      if grid[cart[1][0] - 1][cart[1][1]] == '/':
        cart[0] = 3
      elif grid[cart[1][0] - 1][cart[1][1]] == '\\':
        cart[0] = 1
      elif grid[cart[1][0] - 1][cart[1][1]] == '+':
        if cart[2] == 'l':
          cart[0] = 3
          cart[2] = 's'
        elif cart[2] == 's':
          cart[2] = 'r'
        elif cart[2] == 'r':
          cart[0] = 1
          cart[2] = 'l'
      elif grid[cart[1][0] - 1][cart[1][1]] == '.':
        grid[cart[1][0] - 1][cart[1][1]] = '&'
        print("{}, {}".format(cart[1][0] - 1, cart[1][1]))
        finished = True
        break

      grid[cart[1][0] - 1][cart[1][1]] = '.'
      cart[1] = (cart[1][0] - 1, cart[1][1])
  # printGrid(grid)
  carts = doTheSort(carts)
