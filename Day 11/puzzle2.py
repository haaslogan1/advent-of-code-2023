l = ['...#......', '.......#..', '#.........', '..........', '......#...', '.#........', '.........#', '..........', '.......#..', '#...#.....']

# Read in the actual input (smaller sample input above)
# l = [x for x in open('input.txt').read().strip('\n\n').split('\n')]


x = []

# Horizontally expand the universe
for y in range(1, len(l) + 1):
	
	# check if this line has the string
	# if not, add it to the list of strings that need to be added to l
	if '#' not in l[y - 1]:
		x.append([y-1 , str(l[y - 1])])

# Use the x list from above to shift the universe horizontally
r = 0
for y in x:
	for i in range(0, 9):
		l.insert(y[0] + r, y[1])
		r += 1


x = []
# Veritcally expand the universe
for y in range(0, len(l[0])):
	
	# boolean indicator of whether or not a galaxy was found in the column
	boo = 1
	
	for z in range(0, len(l)):
		
		# check for a galaxy
		# if there is a galaxy ('#'), move on to the next line
		if '#' == list(l[z])[y]:
			boo = 0
			break
			
	# if there was no galaxy in the column, add it to the list of empty columns
	if boo:	
		x.append(y)

	
# Double each column that was found in the x list above
r = 0
for y in x:
	
	# itearate through each row of the universe
	for i in range(0, 9):
		for z in range(0, len(l)):
			
			
			# add the extra . for each column index (y) of each row (z)
			st_list = list(l[z])
	
			st_list.insert(y + r, '.')
	
			l[z] = ''.join(st_list)
			
			# iterate to account for the shifted universe
		r += 1


		
x = []
# find each galaxy iterating through every column index of every row
for z in range(0,len(l)):
	for y in range(0, len(l[z])):
		
		# if there is a galaxy at this location, add it to the list of galaxies
		if l[z][y] == '#':
			x.append([z, y])

# print(x)
# find total distance of each short distance
maxDist = 0
# iterate through every galaxy y
for y in range(0,len(x)):
	# iterate through every galaxy with a higher x,y value than y
	for z in range(y + 1, len(x)):

		# add the shortest possible distance (absolute value of x and y differences) to the total dist
		maxDist += abs(x[z][0] - x[y][0]) + abs(x[z][1] - x[y][1])	
		
print(maxDist)