with open('inputDay4.txt', 'r') as dataset:
	data =  dataset.read().split('\n')
	overlapping = []
	for line in data:
		if line != '':
			lines = line.split(',')
			firstSegments = lines[0].split('-')
			secondSegments = lines[1].split('-')
			if int(firstSegments[0]) <= int(secondSegments[0]) and int(firstSegments[1]) >= int(secondSegments[1]):
				overlapping.append(line)
			elif int(firstSegments[0]) >= int(secondSegments[0]) and int(firstSegments[1]) <= int(secondSegments[1]):
				# print(firstSegments,secondSegments)
				# print(firstSegments[0], secondSegments[0])
				# print(firstSegments[1], secondSegments[1])
				overlapping.append(line)
		
	print(len(overlapping))
		
with open('inputDay4.txt', 'r') as dataset:
	data =  dataset.read().split('\n')
	overlapping = []
	for line in data:
		if line != '':
			lines = line.split(',')
			firstSegments = lines[0].split('-')
			secondSegments = lines[1].split('-')
			if int(firstSegments[1]) < int(secondSegments[0]):
				continue
			elif int(firstSegments[0]) > int(secondSegments[1]):
				continue
			else:
				overlapping.append(line)
	print(len(overlapping))