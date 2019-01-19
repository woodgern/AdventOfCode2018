def distance_from_point(coordx, coordy, x, y):
  return abs(coordx - x) + abs(coordy - y)

with open("aoc-6-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

coords = []

for c in content:
  coordinate = c.split(', ')
  coords.append((int(coordinate[0]), (int(coordinate[1]))))

left = 1000000
right = 0
top = 0
bottom = 1000000
for coord in coords:
  if coord[0] < left:
    left = coord[0]
  if coord[0] > right:
    right = coord[0]
  if coord[1] < bottom:
    bottom = coord[1]
  if coord[1] > top:
    top = coord[1]

grid = [[(max(top, right), None) for x in range(top - bottom)] for y in range(right - left)]

for coord in coords:
  for y in range(top - bottom):
    for x in range(right - left):
      d = distance_from_point(coord[0] - left, coord[1] - bottom, x, y)
      if d < grid[x][y][0]:
        grid[x][y] = (d, coord)
      elif d == grid[x][y][0]:
        grid[x][y] = (d, (-1, -1))

coord_map = {}
for y in range(top - bottom):
  for x in range(right - left):
    if coord_map.get(grid[x][y][1]) is None:
      coord_map[grid[x][y][1]] = 0
    coord_map[grid[x][y][1]] = coord_map[grid[x][y][1]] + 1

loneliest_area = 0
for coord in coords:
  if coord_map[coord] > loneliest_area:
    loneliest_area = coord_map[coord]

print(loneliest_area)
