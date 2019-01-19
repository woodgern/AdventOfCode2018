class Nanobot:
  def __init__(self, x, y, z, r):
    self.x = x
    self.y = y
    self.z = z
    self.r = r

  def intersects(self, bot):
    distance = abs(self.x - bot.x) + abs(self.y - bot.y) + abs(self.z - bot.z)
    return distance != 0 and distance < (self.r + bot.r)

def is_in_range(x1, y1, z1, x2, y2, z2, r):
  return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) <= r

def is_intersecting(bots, x, y, z):
  for bot in bots:
    if not is_in_range(x, y, z, bot.x, bot.y, bot.z, bot.r):
      return False
  return True



with open("aoc-23-1.txt") as f:
  content = f.readlines()

content = [x.strip() for x in content]

bots = []

for line in content:
  posRad = line.split(' ')

  pos = posRad[0].split('=')[1].strip('<').strip('>,').split(',')
  rad = int(posRad[1].split('=')[1])
  bots.append(Nanobot(int(pos[0]), int(pos[1]), int(pos[2]), rad))

bad_group = bots.copy()


while True:
  lowest_intersections = len(bad_group) - 1
  indices = []

  for i in range(len(bad_group)):
    count = 0
    for j in range(len(bad_group)):
      if i != j and bots[i].intersects(bots[j]):
        count += 1
    if count <= lowest_intersections:
      if count == lowest_intersections:
        indices.append(i)
      else:
        indices = [i]
      lowest_intersections = count

  if lowest_intersections == len(bad_group) - 1:
    break

  indices.sort(reverse=True)
  for i in indices:
    bad_group.pop(i)


group = sorted(bad_group, key=lambda bot : bot.r)

print(len(group))

x_low = -100000000000
x_high = 100000000000
y_low = -100000000000
y_high = 100000000000
z_low = -100000000000
z_high = 100000000000
for bot in group:
  if bot.x + bot.r < x_high:
    x_high = bot.x + bot.r
  if bot.x - bot.r > x_low:
    x_low = bot.x - bot.r
  if bot.y + bot.r < y_high:
    y_high = bot.y + bot.r
  if bot.y - bot.r > y_low:
    y_low = bot.y - bot.r
  if bot.z + bot.r < z_high:
    z_high = bot.z + bot.r
  if bot.z - bot.r > z_low:
    z_low = bot.z - bot.r

print("x: {} - {}, y: {} - {}, z: {} - {}".format(x_low, x_high, y_low, y_high, z_low, z_high))

total = 10000000000000000000
for x in range(x_low, x_high + 1):
  for y in range(y_low, y_high + 1):
    for z in range(z_low, z_high + 1):
      if is_intersecting(group, x, y, z) and x + y + z < total:
        total = x + y + z

print(total)
# inter = sorted(inter, key=lambda point : (point[0] + point[1] + point[2]))
# print(inter) 

