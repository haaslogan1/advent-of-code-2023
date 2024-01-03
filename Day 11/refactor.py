# l = ['...#......', '.......#..', '#.........', '..........', '......#...', '.#........', '.........#', '..........', '.......#..', '#...#.....']

# Read in the actual input (smaller sample input above)
l = [x for x in open('input.txt').read().strip('\n\n').split('\n')]


# Horizontally expand the universe
rows = []
for y in range(0, len(l)):
	
	# check if this line has the string
	# if not, add it to the list of strings that need to be added to l
	if '#' not in l[y]:
		rows.append(y)

cols = []
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
		cols.append(y)

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
		
		# If there is a 100000x multiplier row between the locations, simply add 100000 -1 
		for i in rows:
			if (( x[z][0] - x[y][0]) > 0 and x[z][0] > i and x[y][0] < i):
				maxDist += (1000000 - 1)
			elif (( x[z][0] - x[y][0]) < 0 and x[z][0] < i and x[y][0] > i):
				maxDist += (1000000 - 1)
		
		# If there is a 100000x multiplier row between the locations, simply add 100000 -1 
		for i in cols:
			if ((x[z][1] - x[y][1]) > 0 and x[z][1] > i and x[y][1] < i):
				maxDist += (1000000 - 1)
			elif ((x[z][1] - x[y][1]) < 0 and x[z][1] < i and x[y][1] > i):
				maxDist += (1000000 - 1)
		
		# add the shortest possible distance (absolute value of x and y differences) to the total dist
		maxDist += abs(x[z][0] - x[y][0]) + abs(x[z][1] - x[y][1])	
		
print(maxDist)