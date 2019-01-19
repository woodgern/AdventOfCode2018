import numpy as np

with open("aoc-4-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

content.sort()

guards = dict()
guard_totals = dict()
highest_guard_number = 0

guard_number = '#fart'
sleep_start = 0
sleep_end = 0

for notification in content:
	notification_split = notification.split(' ')
	if notification_split[2] == 'Guard':
		guard_number = notification_split[3]
		if int(guard_number.strip('#')) > highest_guard_number:
			highest_guard_number = int(guard_number.strip('#'))
		continue
	elif notification_split[2] == 'falls':
		sleep_start = int(notification[15:17])
		continue
	elif notification_split[2] == 'wakes':
		sleep_end = int(notification[15:17])

	if guards.get(guard_number) is None:
		guards[guard_number] = [0 for x in range(60)]

	if guard_totals.get(guard_number) is None:
		guard_totals[guard_number] = 0

	for i in range(sleep_start, sleep_end):
		guards[guard_number][i] = guards[guard_number][i] + 1

	guard_totals[guard_number] = guard_totals[guard_number] + (sleep_end - sleep_start)

sleepiest_minute = 0
sleepiest_minute_total = 0
sleepiest_guard_number = 0
for i in range(1, highest_guard_number + 1):
	if guards.get('#{}'.format(i)) is not None and guards['#{}'.format(i)][np.argmax(guards['#{}'.format(i)])] > sleepiest_minute_total:
		sleepiest_minute_total = guards['#{}'.format(i)][np.argmax(guards['#{}'.format(i)])]
		sleepiest_minute = np.argmax(guards['#{}'.format(i)])
		sleepiest_guard_number = '#{}'.format(i)

print("sleepiest guard: {}, sleepiest minute: {}, answer: {}".format(sleepiest_guard_number, sleepiest_minute, int(sleepiest_guard_number.strip('#')) * sleepiest_minute))
