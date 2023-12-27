import re

from collections import defaultdict

if __name__ == "__main__":
	
	# Open Input parser
	data = open('input.txt', 'r')
	
	# Get all the seeds and convert them to ints
	seeds = data.readline()
	seeds = re.findall('\d+', seeds)
	seeds = [int(val) for val in seeds]
	
	# Set x to be a temp value storing each line
	x = data.readline()
	
	# 2-D array storing all sources and destinations
	arr = defaultdict(list)
	idx = -1
	
	# Convert conversion chart to a 2-D array containing only src and dest
	while x:
		if '\n' == x:
			x = data.readline()
			continue
		if '-to-' in x:
			idx += 1
			x = data.readline()
			continue
		else:
			tmpArr = []
			
			vals = re.findall('\d+', x)
			
			vals = [int(val) for val in vals]
			
			arr[idx].append(vals)
			
			x = data.readline()
			
			
	
	# Set a very high lowest location
	lowestLocation = 9999999999999999
	tmpLowestLocation = lowestLocation
	
	# Traverse through each seed, each of the seven conversions, and each val of the seven conversions
	for seed in seeds:
		for idx in [0,1,2,3,4,5,6,7]:
			for val in arr[idx]:
			
				if seed >= val[1] and seed <= (val[1] + val[2] - 1):
				
				
				
					# Calculate the difference between seed and the maximum
					x = seed - val[1]
				
					print('seed: ' + str(seed) + '\n' + 'x: ' + str(x) + '\norigin seed: ' + str(val[0]))
					seed = val[0] + x
					tmpLowestLocation = seed
					
					break
		
		# If we find a new low (after the seven conversions), set that
		if tmpLowestLocation < lowestLocation:
			lowestLocation = tmpLowestLocation
	
	# Give me an answer!
	print(lowestLocation)