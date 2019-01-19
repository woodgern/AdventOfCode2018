def differsByOne(id1, id2):
	dirty = False
	for i in range(len(id1)):
		if not dirty and id1[i] != id2[i]:
			dirty = True
		elif dirty and id1[i] != id2[i]:
			return False
	return True

with open("aoc-2-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

previous = []
for eyeD in content:
	for old_id in previous:
		if differsByOne(old_id, eyeD):
			print("{}, {}".format(old_id, eyeD))
			break
	previous.append(eyeD)
# mphcuasvrnjzzkbgdtqeoylva