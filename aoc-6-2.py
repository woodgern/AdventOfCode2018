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

grid = [[(max(top, right), None) for y in range(top + 200)] for x in range(right + 200)]

popularest_area = 0
for y in range(top + 200):
  for x in range(right + 200):
    d = 0 
    for coord in coords:
      d = d + distance_from_point(coord[0], coord[1], x, y)
      if d >= 10000:
        break
    if d < 10000:
      grid[x][y] = 1
      popularest_area = popularest_area + 1

print(popularest_area)
