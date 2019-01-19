inp = 5719

grid = [[0 for y in range(301)] for y in range(301)]


for y in range(1, 301):
  for x in range(1, 301):
    rackId = x + 10
    power_level = rackId * y
    power_level = power_level + inp
    power_level = power_level * rackId

    if len(str(power_level)) < 3:
      hundo = 0
    else:
      hundo = int(str(power_level)[-3])

    grid[x][y] = hundo - 5 + grid[x - 1][y] + grid[x][y - 1] - grid[x - 1][y - 1]

highest = -10000000000000
high_x = 0
high_y = 0
high_size = 0
for size in range(1, 301):
  for y in range(size, 301):
    for x in range(size, 301):
      s = grid[x][y] - grid[x - size][y] - grid[x][y - size] + grid[x - size][y - size]
      if s > highest:
        highest = s
        high_x = x 
        high_y = y
        high_size = size

print("{},{},{}".format(high_x - high_size + 1, high_y - high_size + 1, high_size))
