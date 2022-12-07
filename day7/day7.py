with open('testInput.txt') as dataset:
	data = dataset.read().split('\n')
	# print(data)

	dir = {}
	order = {}
	curLocation = ''
	total2 = 0

	for i in data:
		# print(i)
		if i[0] != '':
			if i[0] == '$':
				# print('command')
				x = i.split()
				# print(x)
				if x[1] == 'cd':
					if x[2] != '..':
						dir[x[2]] = []
						curLocation = ''
						curLocation = x[2]
						# print(curLocation)
					# 	order.append([curLocation])
					
					# print(order)

			elif i[0] == 'd':
				continue
			else:
				# print('file')
				v = i.split(' ')
				# print(v[0])
				# print(curLocation)
				l = dir.get(curLocation)
				# print(type(l))
				l.append(int(v[0]))
				dir[curLocation] = l
		else:
			print('Error')
	# print(dir)
	for q, w in dir.items():
		if w != []:
			# print(q, w)
			if sum(w) <= 100000:
				# print(sum(w))
				total2 += sum(w)
		else:
			continue
	# print(total2)
	# print(order)

with open('testInput.txt') as dataset:
	data = dataset.read().split('\n')

	lineOrder = []
	tempLineOrder = []

	for i in data:
		if i[0] == '$':
			x = i.split(' ')
			if x[1] == 'cd':
				# just add to temp array
				# when .. set temp array to lineOrder
				# also get this temp order and remove last one
				# set to remove dupes?
				if x[2] == '..':
					lineOrder.append(tempLineOrder)
					tempLineOrder.pop()
				else:
					tempLineOrder.append(x[2])

	print(lineOrder)
