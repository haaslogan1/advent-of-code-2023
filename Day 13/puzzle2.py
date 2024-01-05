# commented l is used for the sample

l = [['#.##..##.', '..#.##.#.', "##......#", "##......#", "..#.##.#.", "..##..##.", "#.#.##.#."],\
["#...##..#",\
"#....#..#",\
"..##..###",\
"#####.##.",\
"#####.##.",\
"..##..###",\
"#....#..#"]]

# split the file into a list of strings separated by each new line
# l = [x.split('\n') for x in open('input.txt').read().split('\n\n')]

# initialize the count
coutn = 0

# iterate through each list in l
for x in l:
	

	
	#check for horizontal and vertical lines
	for num in range(1, len(x)):
		
		#mistake count
		mistakes = 0
		
		#initialize the above line count
		lineCount = num
	
		# initialize the idx
		smallNum = num - 1
		
		# while we are still in the range of the list
		while smallNum > -1 and num < len(x):
		
			# comparison strings
			a = x[smallNum]
			b = x[num]
			
			
			for mstk in range(0, len(a)):
				if (list(a)[mstk] != list(b)[mstk]):
					mistakes += 1
					if mistakes > 1:
						lineCount = 0
						break

				
			smallNum -= 1
			num += 1
			
			if mistakes > 1:
				break
			
		if mistakes == 1:
			# add to the counter
			coutn += (100 * lineCount)
			
	
	# Check for vertical lines
	tst = x[0]

	# Iterate through each possible vertical line (len of the string - 1)
	for y in range(1, len(tst)):
		
		# must be only 1 mistake
		mistakes = 0
		
		# if the vertical line will be in the second half of the string
		if (y > (len(tst) / 2)):		
			# save y as a temp num used to add to the total count
			tot = y
			# iterate through each string in the complete list to see if it also matches like the first line
			for z in x:
				# comparison strings 
				a = str(z[y:len(tst)])[::-1]
				b = str(z[int((2 * (y - (len(tst) / 2)))):y])
				
				for mstk in range(0, len(a)):
					if (list(a)[mstk] != list(b)[mstk]):
						mistakes += 1
						if mistakes > 1:
							tot = 0
							break
				if mistakes > 1:
					break
			
			if mistakes == 1:
				coutn += tot
		elif (y <= (len(tst) / 2)):
			# save y as a temp num used to add to the total count
			tot = y
			# iterate through each string in the complete list to see if it also matches like the first line
			for z in x:
				# comparison strings 
				a = str(z[0:y])[::-1]
				b = str(z[y:(y * 2)])
				
				for mstk in range(0, len(a)):
					if (list(a)[mstk] != list(b)[mstk]):
						mistakes += 1
						if mistakes > 1:
							tot = 0
							break
				if mistakes > 1:
					break
			
			if mistakes == 1:
				coutn += tot


print(coutn)
				