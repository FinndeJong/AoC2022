def divide_chunks(l, n):
	for i in range(0, len(l), n):
		yield l[i:i + n]

with open('inputDay3.txt', 'r') as dataset:
	data = dataset.read().split('\n');
	points = []
	points2 = [] 
	for a in data:
		firsthalf = slice(0, len(a)//2)
		secondhalf = slice(len(a)//2, len(a)) 
		# print(a[firsthalf], a[secondhalf])
		lastComp = ''
		for char in a[firsthalf]:
			if char in a[secondhalf]:
				# print(char)
				if char != lastComp:
					lastComp = char
					if char.isupper():
						points.append(ord(char) - 38)
					else:
						# print(char)
						points.append(ord(char) - 96)
	print(sum(points))

	elfgroups = divide_chunks(data, 3)
	temp = []
	for i in elfgroups:
		lastChar = ''
		for char in i[0]:
			if char in i[1]:
				if char != lastChar:
					if char in i[2]:
						lastChar = char
						if char.isupper():
							temp.append(ord(char) - 38)
						else:
							temp.append(ord(char) - 96)
	print(sum(temp))

test = ['AABBCCggg', 'DDEEFFgg', 'HHIIJJgg']
lastChar = ''
for char in test[0]:
	if char != lastChar:
		if char in test[1]:
			if char in test[2]:
				lastChar = char
				print(char)


	# Devide item in half
	# Compare strings for doubles
	# Not doubles in array
	# Convert doubles to priority
	# Add priorities together