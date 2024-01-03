l = ['...#......', '.......#..', '#.........', '..........', '......#...', '.#........', '.........#', '..........', '.......#..', '#...#.....']

for x in l:
	print(x)
print()
# ....#.........
x = []

# Horizontally expand the universe
for y in range(1, len(l) + 1):
	
	# check if this line has the string
	# if not, add it to the list of strings that need to be added to l
	if '#' not in l[y - 1]:
		x.append([y-1 , str(l[y - 1])])

r = 0
for y in x:
	l.insert(y[0] + r, y[1])
	r += 1

# ...........#......


x = []
# Veritcally expand the universe
for y in range(0, len(l[0])):
	boo = 1
	for z in range(0, len(l)):
		
		# check 
		if '#' == list(l[z])[y]:
			boo = 0
			break
			
			
	if boo:
		
		x.append(y)

	
r = 0
for y in x:
	
	for z in range(0, len(l)):
	
		st_list = list(l[z])
		
		st_list.insert(y + r, '.')
		
		l[z] = ''.join(st_list)
		
	r += 1

	
for x in l:
	print(x)
		
x = []
# find each galaxy
for z in range(0,len(l)):
	for y in range(0, len(l[z])):
		
		if l[z][y] == '#':
			x.append([z, y])

# print(x)
# find longest distance
maxDist = 0
for y in range(0,len(x)):
	for z in range(y + 1, len(x)):
# 		if ((abs(x[z][0] - x[y][0]) + abs(x[z][1] - x[y][1])) > maxDist):
		print(str(x[y]) + ' ' + str(x[z]))
		
		dist = abs(x[z][0] - x[y][0]) + abs(x[z][1] - x[y][1])
		print(dist)
		maxDist += dist	
		
print(maxDist)