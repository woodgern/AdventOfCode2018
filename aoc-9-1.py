class Marble:

  def __init__(self, cw, ccw, value):
    self.cw = cw
    self.ccw = ccw
    self.value = value


player_count = 423
last_marble_value = 7194400

player_scores = {}

for i in range(1, player_count + 1):
  player_scores[i] = 0

current = Marble(None, None, 0)
current.cw = current
current.ccw = current

current_player = 1
marble_number = 1
while True:
  if marble_number % 23 != 0:
    clockwise = current.cw
    prev_next = clockwise.cw
    clockwise.cw = Marble(prev_next, clockwise, marble_number)
    prev_next.ccw = clockwise.cw
    current = clockwise.cw
  else:
    next_current = current.ccw.ccw.ccw.ccw.ccw.ccw
    removed = next_current.ccw
    beside = next_current.ccw.ccw
    beside.cw = next_current
    next_current.ccw = beside
    current = next_current

    points = marble_number + removed.value
    player_scores[current_player] = player_scores[current_player] + points

    if marble_number + 23 > last_marble_value:
      break

  if current_player < player_count:
    current_player = current_player + 1
  else:
    current_player = 1
  marble_number = marble_number + 1

winner = 0
for i in range(1, player_count + 1):
  if player_scores[i] > winner:
    winner = player_scores[i]

print(winner)
