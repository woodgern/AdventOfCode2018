import copy
import sys

def doTheRemove(carts):
  s3 = []
  for i in range(len(carts)):
    for j in range(len(carts)):
      if i != j:
        if carts[i][1] == carts[j][1]:
          s3.append(i)
          s3.append(j)
  s4 = []
  for i in range(len(s2)):
    if i not in s3:
      s4.append(s2[i])
  return s4

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

grid = [['' for y in range(155)] for x in range(155)]
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

    grid[column][line_count] = char
    column += 1
  line_count += 1


with open("aoc-13-1-2.txt") as f:
    content = f.readlines()

content = [x for x in content]

og_grid = [['' for y in range(155)] for x in range(155)]

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

tick = 0
finished = False

while not finished:
  k = 0
  while k < len(carts):
    cart = carts[k]
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
      if grid[cart[1][0]][cart[1][1] - 1] == '.':
        grid[cart[1][0]][cart[1][1] - 1] = og_grid[cart[1][0]][cart[1][1] - 1]
        print("{}, {}".format(cart[1][0], cart[1][1] - 1))
        cart[1] = (cart[1][0], cart[1][1] - 1)

        s3 = []
        for a in range(len(carts)):
          for b in range(len(carts)):
            if a != b:
              if carts[a][1] == carts[b][1]:
                s3.append(a)
                s3.append(b)
                grid[carts[a][1][0]][carts[a][1][1]] = og_grid[carts[a][1][0]][carts[a][1][1]]
                grid[carts[b][1][0]][carts[b][1][1]] = og_grid[carts[b][1][0]][carts[b][1][1]]
                if (a < k or b < k):
                  k -= 1
                break
        s4 = []
        for a in range(len(carts)):
          if a not in s3:
            s4.append(carts[a])
        carts = s4
        k -= 1
      else:
        grid[cart[1][0]][cart[1][1] - 1] = og_grid[cart[1][0]][cart[1][1] - 1]
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
      if grid[cart[1][0] + 1][cart[1][1]] == '.':
        grid[cart[1][0] + 1][cart[1][1]] = og_grid[cart[1][0] + 1][cart[1][1]]
        print("{}, {}".format(cart[1][0] + 1, cart[1][1]))
        cart[1] = (cart[1][0] + 1, cart[1][1])

        s3 = []
        for a in range(len(carts)):
          for b in range(len(carts)):
            if a != b:
              if carts[a][1] == carts[b][1]:
                s3.append(a)
                s3.append(b)
                grid[carts[a][1][0]][carts[a][1][1]] = og_grid[carts[a][1][0]][carts[a][1][1]]
                grid[carts[b][1][0]][carts[b][1][1]] = og_grid[carts[b][1][0]][carts[b][1][1]]
                if (a < k or b < k):
                  k -= 1
                break
        s4 = []
        for a in range(len(carts)):
          if a not in s3:
            s4.append(carts[a])
        carts = s4
        k -= 1
      else:
        grid[cart[1][0] + 1][cart[1][1]] = og_grid[cart[1][0] + 1][cart[1][1]]
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
      if grid[cart[1][0]][cart[1][1] + 1] == '.':
        grid[cart[1][0]][cart[1][1] + 1] = og_grid[cart[1][0]][cart[1][1] + 1]
        print("{}, {}".format(cart[1][0], cart[1][1] + 1))
        cart[1] = (cart[1][0], cart[1][1] + 1)

        s3 = []
        for a in range(len(carts)):
          for b in range(len(carts)):
            if a != b:
              if carts[a][1] == carts[b][1]:
                s3.append(a)
                s3.append(b)
                grid[carts[a][1][0]][carts[a][1][1]] = og_grid[carts[a][1][0]][carts[a][1][1]]
                grid[carts[b][1][0]][carts[b][1][1]] = og_grid[carts[b][1][0]][carts[b][1][1]]
                if (a < k or b < k):
                  k -= 1
                break
        s4 = []
        for a in range(len(carts)):
          if a not in s3:
            s4.append(carts[a])
        carts = s4
        k -= 1
      else:
        grid[cart[1][0]][cart[1][1] + 1] = og_grid[cart[1][0]][cart[1][1] + 1]
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
      if grid[cart[1][0] - 1][cart[1][1]] == '.':
        grid[cart[1][0] - 1][cart[1][1]] = og_grid[cart[1][0] - 1][cart[1][1]]
        print("{}, {}".format(cart[1][0] - 1, cart[1][1]))
        cart[1] = (cart[1][0] - 1, cart[1][1])

        s3 = []
        for a in range(len(carts)):
          for b in range(len(carts)):
            if a != b:
              if carts[a][1] == carts[b][1]:
                s3.append(a)
                s3.append(b)
                if (a < k or b < k):
                  k -= 1
                break
        s4 = []
        for a in range(len(carts)):
          if a not in s3:
            s4.append(carts[a])
        carts = s4
        k -= 1
      else:
        grid[cart[1][0] - 1][cart[1][1]] = og_grid[cart[1][0] - 1][cart[1][1]]
        grid[cart[1][0] - 1][cart[1][1]] = '.'
        cart[1] = (cart[1][0] - 1, cart[1][1])

    k += 1
  # printGrid(grid)
  # print(len(carts))
  carts = doTheSort(carts)
  if len(carts) == 1:
    print(carts)
    break
