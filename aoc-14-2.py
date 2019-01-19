def stringify(ints):
	string = ""
	for i in ints:
		string += str(i)
	return string

recipes = [3, 7]

claim = "110201"

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
	if (currentCount > 6):
		if stringify(recipes[currentCount - 7:currentCount - 1]) == claim:
			print(currentCount - 7)
			print(recipes[currentCount - 7:currentCount - 1])
			break
		if stringify(recipes[currentCount - 6:]) == claim:
			print(currentCount - 6)
			print(recipes[currentCount - 6:])
			break

