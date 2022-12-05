with open('inputDay5.txt', 'r') as dataset:
	ground = {
		1: ['R', 'P', 'C', 'D', 'B', 'G'],
		2: ['H', 'V', 'G'],
		3: ['N', 'S', 'Q', 'D', 'J', 'P', 'M'],
		4: ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'],
		5: ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'],
		6: ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'],
		7: ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'],
		8: ['C', 'M', 'D', 'B', 'F'],
		9: ['F', 'C', 'Q', 'G']
	}
	data = dataset.read().split('\n')
	for i in data:
		if i != '':
			r = i.split(' ')
			r.remove(r[4])
			r.remove(r[2])
			r.remove(r[0])
			for x in range(int(r[0])):
				oldRow = ground.get(int(r[1]))
				newRow = ground.get(int(r[2]))
				newRow.insert(len(newRow), oldRow[-1])
				oldRow.pop()
	# print(ground)

with open('inputDay5.txt', 'r') as dataset:
	ground = {
		1: ['R', 'P', 'C', 'D', 'B', 'G'],
		2: ['H', 'V', 'G'],
		3: ['N', 'S', 'Q', 'D', 'J', 'P', 'M'],
		4: ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'],
		5: ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'],
		6: ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'],
		7: ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'],
		8: ['C', 'M', 'D', 'B', 'F'],
		9: ['F', 'C', 'Q', 'G']
	}
	data = dataset.read().split('\n')
	for i in data:
		if i != '':
			r = i.split(' ')
			r.remove(r[4])
			r.remove(r[2])
			r.remove(r[0])
			oldRow = ground.get(int(r[1]))
			newRow = ground.get(int(r[2]))
			temp = []
			for x in range(int(r[0])):
				temp.append(oldRow[-x-1])
			temp.reverse()
			for l in temp:
				newRow.insert(len(newRow), l)
				oldRow.pop()	
	print(ground)