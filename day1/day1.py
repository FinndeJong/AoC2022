# Get data

# loop door alle lines
	# alle lines tussen witregel in array zetten
	# array bij elkaar op tellen
	# vergelijken met andere optellingen
	# hoogste printen

# Part 1
with open('inputDay1.txt', 'r') as data:
	temp = []
	total = []
	for line in data:
		if len(line) < 3:
			total.append(sum(map(int, temp)))
			temp.clear()
			# print(total)
		else:
			temp.append(line)
			# print(temp)
	# Part 1
	print(max(total))
	# Part 2
	total.sort() 
	print(total[-3:])
	print(sum(map(int, total[-3:])))