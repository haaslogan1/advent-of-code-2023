import re




if __name__ == "__main__":
	
	
	
	# Open Input parser
	data = open('../input.txt', 'r')
	infile = data.readlines()
	
	# start the total count at 0
	coutn = 0

	
	
	# Loop through each line of input
	for i in infile:
		
		
		# create rgb array
		rgb =[0,0,0]
		
		# open a parser for the line
		# split the ID and colors sections
		line = i.split(':')
		IDstr = line[0]
		colorstr = line[1]
		
		
		# get the ID
		val = int(re.search(r'\d+', IDstr).group())
		
		
		# get amt of cubes for color for each draw - delimit by ';'
		for color in colorstr.split(';'):
			
			# split into each color
			each = color.split(',')
			#print(each)
			
			# Check each comma-seperated color for the amt
			for x in each:
				if 'blue' in x:
					rgb[2] = int(re.search(r'\d+', x).group())
				if 'red' in x:
					rgb[0] =  int(re.search(r'\d+', x).group())
				if 'green' in x:
					rgb[1] =  int(re.search(r'\d+', x).group())
		
			if (rgb[2] > 14 or rgb [1] > 13 or rgb[0] > 12):
				val = 0
				break
			
				
		
		print(val)
		# add the count
		coutn += val
			
	# print the total amt of IDs
	
	print(coutn)
		