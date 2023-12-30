# Idea: Create a queue containing the directions
# Create a list of all the mappings
# Traverse through the queue until we hit 'ZZZ'

import re

# function to find the current string
def fin(strng, mappings):
	for i in range(0, len(mappings)):
		if mappings[i][0] == strng:
			return i
	
	# should never happen
	return -1

# Open the input file
content =  open('input.txt')

# Read in the queue containing directions
queue = list(content.readline())

# Skip a empty line
content.readline()

# Create list of all mappings
mappings = []
for line in content:
	mappings.append(re.findall(r'[A-Z]+', line))

# Convert directions to indeces in the mappings list
for i in range(0, len(queue)):
	match queue[i]:
		case 'L':
			queue[i] = 1
		case 'R':
			queue[i] = 2


currentStr = 'AAA'
currentIdx = fin(currentStr, mappings)
coutn = 0
print(queue)
while 1:
	for i in queue:
		# Skip the new line character
		if i == '\n':
			continue
			
		# Get the current string and iterate the count
		currentStr = mappings[currentIdx][i]
		coutn += 1
		
		# Check if we are done
		if currentStr == 'ZZZ':
			print(coutn)
			break
		
		# Get the new current Idx
		currentIdx = fin(currentStr, mappings)
	
	# Check if we are done
	if currentStr == 'ZZZ':
		break