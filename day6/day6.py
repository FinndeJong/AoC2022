with open('inputDay6.txt') as dataset:
	data = dataset.read()
	curIteration = 0
	marker = []
	for i in data:
		curIteration = curIteration + 1
		marker.append(i)
		if len(marker) == 4:
			if len(marker) == len(set(marker)):
				print(i)
				print(curIteration)
			else:
				marker.pop(0)

with open('inputDay6.txt') as dataset:
	data = dataset.read()
	curIteration = 0
	marker = []
	for i in data:
		curIteration = curIteration + 1
		marker.append(i)
		if len(marker) == 14:
			if len(marker) == len(set(marker)):
				print(i)
				print(curIteration)
			else:
				marker.pop(0)