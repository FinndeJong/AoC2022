with open('inputDay7.txt') as dataset:
	data = dataset.read().split('\n')
	parent = {}
	dupeCheck = set()
	it = []
	for i in data:
		if i[:4] == '$ cd':
			x = i.split(' ')[2]
			if x != '..':
				dupeCheck.add(x)
				parent[x] = {'children': [], 'size': []}
				it.append(x)
				print(it)
				for j in it:
					if j != x:
						par = parent[j]
						f = par.get('children')
						f.append(x)
			else:
				it.pop()
				continue

		
		elif i[0].isdigit() == True:
			a = i.split(' ')[0]
			par = parent[it[-1]].get('size')
			if par != []:
				tempTotal = sum(par) + int(a)
				par.clear()
				par.append(tempTotal)
			else:
				par.append(int(a))
		

	
	# print(dupeCheck)
	# print(parent)

deel1 = []
remaining = []

for k, v in parent.items():
	if v.get('children') != [] and v.get('size') != []:
		if v.get('size')[0] <= 100000:
			deel1.append(v.get('size')[0])
			remaining.append(v)
	elif v.get('children') == [] and v.get('size') != []:
		if v.get('size')[0] <= 100000:
			deel1.append(v.get('size')[0])
for p in remaining:
	for b in p.get('children'):
		if parent.get(b).get('children') == []:
			if parent.get(b).get('size')[0] <= 100000:
				deel1.append(parent.get(b).get('size')[0])

print(sum(deel1))
print(remaining)
