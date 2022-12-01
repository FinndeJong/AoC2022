with open('inputDay1.txt', 'r') as data:
	temp = []
	total = []
	for line in data:
		if len(line) < 3:
			total.append(sum(map(int, temp)))
			temp.clear()
		else:
			temp.append(line)
	# Part 1
	print(max(total))
	# Part 2
	total.sort() 
	print(total[-3:])
	print(sum(map(int, total[-3:])))