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
		tmp = [0,0,0]
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
					tmp[2] = int(re.search(r'\d+', x).group())
					if (tmp[2] > rgb[2]):
						rgb[2] = tmp[2]
				if 'red' in x:
					tmp[0] =  int(re.search(r'\d+', x).group())
					if tmp[0] > rgb[0]:
						rgb[0] = tmp[0]
				if 'green' in x:
					tmp[1] =  int(re.search(r'\d+', x).group())
					if tmp[1] > rgb[1]:
						rgb[1] = tmp[1]

		
		# calculate and add the power
		coutn += (rgb[0] * rgb[1] * rgb[2])
			
	# print the total amt of IDs
	
	print(coutn)
		