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
						curLocation = x[2]
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
	print(dir)

	# print(curLocation)

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

# with open('testInput.txt') as dataset:
# 	data = dataset.read().split('\n')

# 	folderTree = {
# 		'/': {}
# 	}
# 	curLocation = [['/']]

# 	# print(data)
# 	# Read every liness
# 	for i in data:
# 		if i[0] == '$':
# 			if i == '$ cd /' or i == '$ ls':
# 				continue
# 			else:
# 				s = i.split(' ')
# 				if s[2] == '..':
# 					curLocation.pop()
# 				else:
# 					curLocation.append([s[2]])
# 			print(curLocation)

# 		if i[0] == 'd':
# 			s = i.split(' ')
# 			# print(curLocation)

# 			dataFromTree = folderTree
# 			for l in curLocation:
# 				print(dataFromTree)
# 				# dataFromTree = dataFromTree[l[0]]

