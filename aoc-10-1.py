def pointDensity(vectors):
  total_dist = 0
  for i in range(len(vectors)):
    for j in range(len(vectors)):
      if i != j:
        dist = (((vectors[i][0][0] - vectors[j][0][0])**2) + ((vectors[i][0][1] - vectors[j][0][1])**2))**(0.5)
        total_dist = total_dist + dist

  return total_dist / len(vectors)

def printGrid(grid, top, right):
  for y in range(top):
    for x in range(right):
      if(grid[x][y] == 0):
        print('.', end='')
      else:
        print('#', end='')
    print('\n', end='')

with open("aoc-10-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

vectors = []

for line in content:
  line = line.replace('<', ', ').replace('>', ', ')
  line_arr = line.split(', ')
  vectors.append(((float(line_arr[1]), float(line_arr[2])), (float(line_arr[4]), float(line_arr[5]))))

densest = None
highest_density = 100000000000000
ticks = 10312
tick_factor = 1

for i in range(len(vectors)):
  new_vector = ((vectors[i][0][0] + vectors[i][1][0]*ticks, vectors[i][0][1] + vectors[i][1][1]*ticks), vectors[i][1])
  vectors[i] = new_vector


# while True:
#   density = pointDensity(vectors)

#   if density < highest_density:
#     highest_density = density

#   if density > highest_density:
#     break

#   for i in range(len(vectors)):
#     new_vector = ((vectors[i][0][0] + vectors[i][1][0]*tick_factor, vectors[i][0][1] + vectors[i][1][1]*tick_factor), vectors[i][1])
#     vectors[i] = new_vector
#   ticks = ticks + tick_factor

left = 0
right = 0
top = 0
bottom = 0
for vector in vectors:
  if vector[0][0] < left:
    left = int(vector[0][0])
  if vector[0][0] > right:
    right = int(vector[0][0])
  if vector[0][1] < bottom:
    bottom = int(vector[0][1])
  if vector[0][1] > top:
    top = int(vector[0][1])

grid = [[0 for i in range(top + 20)] for j in range(right + 20)]

for vector in vectors:
  x = int(vector[0][0])
  y = int(vector[0][1])
  grid[x][y] = 1

printGrid(grid, top + 20, right + 20)

print(ticks)

