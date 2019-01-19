class Nanobot:
  def __init__(self, x, y, z, r):
    self.x = x
    self.y = y
    self.z = z
    self.r = r

def is_in_range(x1, y1, z1, x2, y2, z2, r):
  return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) <= r


with open("aoc-23-1.txt") as f:
  content = f.readlines()

content = [x.strip() for x in content]

bots = []

for line in content:
  posRad = line.split(' ')

  pos = posRad[0].split('=')[1].strip('<').strip('>,').split(',')
  rad = int(posRad[1].split('=')[1])
  bots.append(Nanobot(int(pos[0]), int(pos[1]), int(pos[2]), rad))

big_bot = None
for i in range(len(bots)):
  if big_bot is None or bots[i].r > big_bot.r:
    big_bot = bots[i]

count = 0
for i in range(len(bots)):
  if is_in_range(bots[i].x, bots[i].y, bots[i].z, big_bot.x, big_bot.y, big_bot.z, big_bot.r):
    count += 1

print(count)
