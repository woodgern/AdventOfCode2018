recipes = [3, 7]

claim = 110201

current1 = 0
current2 = 1

currentCount = 2
while True:
	# combine the recipes
	sumNum = str(recipes[current1] + recipes[current2])
	for c in sumNum:
		currentCount += 1
		recipes.append(int(c))

	current1 = (recipes[current1] + 1 + current1) % currentCount
	current2 = (recipes[current2] + 1 + current2) % currentCount

	if currentCount >= claim + 10:
		break

print(recipes[110201:110201+10])
