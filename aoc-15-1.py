import copy

class Unit:
  def __init__(self, hp, ap, team, x, y):
    self.hp = hp
    self.ap = ap
    self.team = team
    self.x = x
    self.y = y
    self.alive = True

  def damage(self, amount):
    self.hp = self.hp - amount

def sortCombatants(units):
  s1 = sorted(units, key=lambda unit: unit.x)
  return sorted(s1, key=lambda unit: unit.y)

def printGrid(grid):
  for y in range(32):
    for x in range(32):
      print(grid[x][y], end='')
    print()

def fill(grid, x, y):
  if grid[x][y] == 'E' or grid[x][y] == 'G':
    grid[x][y] = 0
  else: 
    top, bottom, left, right = 150, 150, 150, 150
    if isinstance(grid[x - 1][y], int):
      left = grid[x - 1][y]
    if isinstance(grid[x + 1][y], int):
      right = grid[x + 1][y]
    if isinstance(grid[x][y - 1], int):
      top = grid[x][y - 1]
    if isinstance(grid[x][y + 1], int):
      bottom = grid[x][y + 1]

    grid[x][y] = min(top, bottom, right, left) + 1

  if grid[x - 1][y] == '.' or (isinstance(grid[x - 1][y], int) and grid[x][y] + 1 < grid[x - 1][y]):
    fill(grid, x - 1, y)
  if grid[x + 1][y] == '.' or (isinstance(grid[x + 1][y], int) and grid[x][y] + 1 < grid[x + 1][y]):
    fill(grid, x + 1, y)
  if grid[x][y - 1] == '.' or (isinstance(grid[x][y - 1], int) and grid[x][y] + 1 < grid[x][y - 1]):
    fill(grid, x, y - 1)
  if grid[x][y + 1] == '.' or (isinstance(grid[x][y + 1], int) and grid[x][y] + 1 < grid[x][y + 1]):
    fill(grid, x, y + 1)

def chooseStep(grid, x, y):
  if grid[x][y] == 1:
    return (x, y)

  smallest = grid[x][y]
  small_x = 0
  small_y = 0
  if isinstance(grid[x][y - 1], int) and grid[x][y - 1] < smallest:
    smallest = grid[x][y - 1]
    small_x = x
    small_y = y - 1
  if isinstance(grid[x - 1][y], int) and grid[x - 1][y] < smallest:
    smallest = grid[x - 1][y]
    small_x = x - 1
    small_y = y
  if isinstance(grid[x + 1][y], int) and grid[x + 1][y] < smallest:
    smallest = grid[x + 1][y]
    small_x = x + 1
    small_y = y
  if isinstance(grid[x][y + 1], int) and grid[x][y + 1] < smallest:
    smallest = grid[x][y + 1]
    small_x = x
    small_y = y + 1


  possible_paths = []
  if isinstance(grid[x][y - 1], int) and grid[x][y - 1] == smallest:
    possible_paths.append(chooseStep(grid, x, y - 1))
  if isinstance(grid[x - 1][y], int) and grid[x - 1][y] == smallest:
    possible_paths.append(chooseStep(grid, x - 1, y))
  if isinstance(grid[x + 1][y], int) and grid[x + 1][y] == smallest:
    possible_paths.append(chooseStep(grid, x + 1, y))
  if isinstance(grid[x][y + 1], int) and grid[x][y + 1] == smallest:
    possible_paths.append(chooseStep(grid, x, y + 1))

  s1 = sorted(possible_paths, key=lambda path: path[0])
  s2 = sorted(s1, key=lambda path: path[1])
  return s2[0]

def isReadier(x1, y1, x2, y2):
  if y1 < y2:
    return True
  if y1 == y2 and x1 < x2:
    return True

def choose_target(units, x, y, g, target_team):
  grid = copy.deepcopy(g)
  fill(grid, x, y)

  target = None
  target_dist = 150
  target_x = 0
  target_y = 0
  target_hp = 201
  target_hp2 = 201
  engaged = False
  for unit in units:
    if unit.x == x and unit.y == y or unit.team != target_team or not unit.alive:
      continue

    if ((abs(unit.x - x) + abs(unit.y - y)) == 1) and ((unit.hp == target_hp2 and isReadier(unit.x, unit.y, target_x, target_y)) or unit.hp < target_hp2):
      target = unit
      target_x = target.x
      target_y = target.y
      target_hp2 = target.hp
      engaged = True
      continue

    if not engaged: 
      if isinstance(grid[unit.x][unit.y - 1], int) and grid[unit.x][unit.y - 1] < target_dist:
        target = unit
        target_dist = grid[unit.x][unit.y - 1]
        target_x = unit.x
        target_y = unit.y - 1
        target_hp = target.hp
      if isinstance(grid[unit.x - 1][unit.y], int) and grid[unit.x - 1][unit.y] < target_dist:
        target = unit
        target_dist = grid[unit.x - 1][unit.y]
        target_x = unit.x - 1
        target_y = unit.y
        target_hp = target.hp
      if isinstance(grid[unit.x + 1][unit.y], int) and grid[unit.x + 1][unit.y] < target_dist:
        target = unit
        target_dist = grid[unit.x + 1][unit.y]
        target_x = unit.x + 1
        target_y = unit.y
        target_hp = target.hp
      if isinstance(grid[unit.x][unit.y + 1], int) and grid[unit.x][unit.y + 1] < target_dist:
        target = unit
        target_dist = grid[unit.x][unit.y + 1]
        target_x = unit.x
        target_y = unit.y + 1
        target_hp = target.hp


      if isinstance(grid[unit.x][unit.y - 1], int) and grid[unit.x][unit.y - 1] == target_dist and isReadier(unit.x, unit.y - 1, target_x, target_y):
        target = unit
        target_dist = grid[unit.x][unit.y - 1]
        target_x = unit.x
        target_y = unit.y - 1
        target_hp = target.hp
      if isinstance(grid[unit.x - 1][unit.y], int) and grid[unit.x - 1][unit.y] == target_dist and isReadier(unit.x - 1, unit.y, target_x, target_y):
        target = unit
        target_dist = grid[unit.x - 1][unit.y]
        target_x = unit.x - 1
        target_y = unit.y
        target_hp = target.hp
      if isinstance(grid[unit.x + 1][unit.y], int) and grid[unit.x + 1][unit.y] == target_dist and isReadier(unit.x + 1, unit.y, target_x, target_y):
        target = unit
        target_dist = grid[unit.x + 1][unit.y]
        target_x = unit.x + 1
        target_y = unit.y
        target_hp = target.hp
      if isinstance(grid[unit.x][unit.y + 1], int) and grid[unit.x][unit.y + 1] == target_dist and isReadier(unit.x, unit.y + 1, target_x, target_y):
        target = unit
        target_dist = grid[unit.x][unit.y + 1]
        target_x = unit.x
        target_y = unit.y + 1
        target_hp = target.hp


      if isinstance(grid[unit.x][unit.y - 1], int) and grid[unit.x][unit.y - 1] == 1 and unit.hp < target_hp and unit.x == target_x and unit.y - 1 == target_y:
        target = unit
        target_dist = grid[unit.x][unit.y - 1]
        target_x = unit.x
        target_y = unit.y - 1
        target_hp = target.hp
      if isinstance(grid[unit.x - 1][unit.y], int) and grid[unit.x - 1][unit.y] == 1 and unit.hp < target_hp and unit.x - 1 == target_x and unit.y == target_y:
        target = unit
        target_dist = grid[unit.x - 1][unit.y]
        target_x = unit.x - 1
        target_y = unit.y
        target_hp = target.hp
      if isinstance(grid[unit.x + 1][unit.y], int) and grid[unit.x + 1][unit.y] == 1 and unit.hp < target_hp and unit.x + 1 == target_x and unit.y == target_y:
        target = unit
        target_dist = grid[unit.x + 1][unit.y]
        target_x = unit.x + 1
        target_y = unit.y
        target_hp = target.hp
      if isinstance(grid[unit.x][unit.y + 1], int) and grid[unit.x][unit.y + 1] == 1 and unit.hp < target_hp and unit.x == target_x and unit.y + 1 == target_y:
        target = unit
        target_dist = grid[unit.x][unit.y + 1]
        target_x = unit.x
        target_y = unit.y + 1
        target_hp = target.hp

  next_x, next_y = 0, 0
  if not engaged and target_x != 0:
    next_x, next_y = chooseStep(grid, target_x, target_y)


  return (target, next_x, next_y)

def isBeside(unit1, unit2):
  return abs(unit1.x - unit2.x) + abs(unit1.y - unit2.y) == 1

def enemy(team):
  if team == 'G':
    return 'E'
  return 'G'

def mono_team(units):
  team = units[0].team
  for unit in units:
    if unit.team != team:
      return False
  return True

def printUnits(units):
  for unit in units:
    print("{}({}) | ({},{})".format(unit.team, unit.hp, unit.x, unit.y))


with open("aoc-15-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

grid = [['' for y in range(32)] for x in range(32)]

units = []
y = 0
for line in content:
  x = 0
  for c in line:
    grid[x][y] = c
    if grid[x][y] == 'G':
      units.append(Unit(200, 3, 'G', x, y))
    elif grid[x][y] == 'E':
      units.append(Unit(200, 3, 'E', x, y))
    x += 1
  y += 1

murder_in_progress = True
round_number = 0
while murder_in_progress:
  units = sortCombatants(units)
  # print("Round {}".format(round_number))
  # printGrid(grid)
  # printUnits(units)
  # print()
  for combatant in units:
    if combatant.alive:
      target, next_x, next_y = choose_target(sortCombatants(units.copy()), combatant.x, combatant.y, grid, enemy(combatant.team))
      if (target is None):
        continue

      if (next_x != combatant.x or next_y != combatant.y) and (next_x != 0 or next_y != 0):
        grid[combatant.x][combatant.y] = '.'
        grid[next_x][next_y] = combatant.team
        combatant.x = next_x
        combatant.y = next_y

      if isBeside(combatant, target):
        target.damage(combatant.ap)
        if target.hp <= 0:
          target.alive = False
          grid[target.x][target.y] = '.'
  units = list(filter(lambda unit: unit.alive, units))
  if mono_team(units):
    break
  round_number += 1

health_pool = 0
for unit in units:
  health_pool += unit.hp
print("Combat complete after {} rounds with {} health left".format(round_number, health_pool))
print(health_pool * round_number)
printGrid(grid)
printUnits(units)
























