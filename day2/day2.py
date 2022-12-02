with open('inputDay2.txt', 'r') as dataset:
	data = dataset.read().split('\n')
	#	Points winnig, losing and tie
	win = sum(map(data.count, ('A Y', 'B Z', 'C X'))) * 6
	tie = sum(map(data.count, ('A X', 'B Y', 'C Z'))) * 3
	loss = sum(map(data.count, ('A Z', 'B X', 'C Y'))) * 0

	# Points Choices
	choiceX = sum('X' in i for i in data) * 1
	choiceY = sum('Y' in i for i in data) * 2
	choiceZ = sum('Z' in i for i in data) * 3

	# Total points
	print(win + tie + loss + choiceX + choiceY + choiceZ)

with open('inputDay2.txt', 'r') as dataset:
	data = dataset.read().split('\n')

	#	Points winnig, losing and tie
	win = sum('Z' in i for i in data) * 6
	tie = sum('Y' in i for i in data) * 3
	lolss = sum('X' in i for i in data) * 0

	# Points Choices
	points = 0
	for i in data:
		if 'Y' in i:
			if i[0] == 'A':
				points += 1
			elif i[0] == 'B':
				points += 2
			elif i[0] == 'C':
				points += 3
		elif 'Z' in i:
			if i[0] == 'A':
				points += 2
			elif i[0] == 'B':
				points += 3
			elif i[0] == 'C':
				points += 1
		elif 'X' in i:
			if i[0] == 'A':
				points += 3
			elif i[0] == 'B':
				points += 1
			elif i[0] == 'C':
				points += 2
	
	# Total
	print(win + tie + loss + points)