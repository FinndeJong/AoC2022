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
			print(r)
			for x in range(int(r[0])):
				oldRow = ground.get(int(r[1]))
				newRow = ground.get(int(r[2]))
				newRow.insert(len(newRow), oldRow[-1])
				oldRow.remove(oldRow[-1])
				# print(oldRow, newRow)

testx = {1: ['a', 'b', 'c'], 2: ['d', 'e', 'f', 'a', 'b']}
testz = [[3, 2, 1],[8, 1, 2]]
for i in testz:
	for x in range(i[0]):
		print(x)
		oldRow = testx.get(i[1])
		newRow = testx.get(i[2])
		newRow.insert(len(newRow), oldRow[-1])
		oldRow.remove(oldRow[-1])
		print(testx)
print(testx)

# one = ['R', 'P', 'C', 'D', 'B', 'G']
# two = ['H', 'V', 'G']
# three = ['N', 'S', 'Q', 'D', 'J', 'P', 'M']
# four = ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M']
# five = ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S']
# six = ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S']
# seven = ['B', 'Z', 'M', 'H', 'F', 'T', 'Q']
# eight = ['C', 'M', 'D', 'B', 'F']
# nine = ['F', 'C', 'Q', 'G']