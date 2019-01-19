inp = 7165

grid = [[0 for y in range(300)] for y in range(300)]


for y in range(300):
  for x in range(300):
    rackId = x + 11
    power_level = rackId * (y + 1)
    power_level = power_level + inp
    power_level = power_level * rackId

    if len(str(power_level)) < 3:
      hundo = 0
    else:
      hundo = int(str(power_level)[-3])

    grid[x][y] = hundo - 5

highest = -10000000000000
high_x = 0
high_y = 0
high_size = 0
for size in range(1, 300):
  print("Size: {}".format(size))
  for y in range(300 - size + 1):
    for x in range(300 - size + 1):
      s = 0
      for i in range(size):
        for j in range(size):
          s += grid[x + i][y + j]
      if s > highest:
        highest = s
        high_x = x + 1
        high_y = y + 1
        high_size = size
        print("    {},{},{}".format(high_x, high_y, high_size))

print("{},{},{}".format(high_x, high_y, high_size))
