# commented l is used for the sample

# l = [['#.##..##.', '..#.##.#.', "##......#", "##......#", "..#.##.#.", "..##..##.", "#.#.##.#."],\
# ["#...##..#",\
# "#....#..#",\
# "..##..###",\
# "#####.##.",\
# "#####.##.",\
# "..##..###",\
# "#....#..#"]]

# split the file into a list of strings separated by each new line
l = [x.split('\n') for x in open('input.txt').read().split('\n\n')]

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
		
			# comparison strings for simplicity
			a = x[smallNum]
			b = x[num]
			
			# there will be one '\n' at the end of the l list
			# just using try/except to bypass accounting for that
			try:
				# iterate through the length of a to count unequal chars ("mistakes")
				for mstk in range(0, len(a)):
					# check for unequal characters
					if (list(a)[mstk] != list(b)[mstk]):
						mistakes += 1
						# there can only be one mistake!
						if mistakes > 1:
							lineCount = 0
							break
			except: pass
				
			# iterate the top and bottom row indeces
			smallNum -= 1
			num += 1
			
			# save time, if there is already more than one mistake
			if mistakes > 1:
				break
		
		# we only add to the total count if there is one smudge ("mistake")
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
				
				# iterate through all characters of the comparison strings
				for mstk in range(0, len(a)):
					# check for a smudge
					if (list(a)[mstk] != list(b)[mstk]):
						mistakes += 1
						
						# there can only be one smudge!
						if mistakes > 1:
							tot = 0
							break
				# there can only be one smudge!
				# save time by breaking the loop
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
				
				# iterate through all characters of the comparison strings
				for mstk in range(0, len(a)):
					# check for a smudge
					if (list(a)[mstk] != list(b)[mstk]):
						mistakes += 1
						# there can only be one smudge!
						if mistakes > 1:
							tot = 0
							break
				# there can only be one smudge!
				# save time by breaking the loop
				if mistakes > 1:
					break
			
			# there must be exactly one smudge!
			if mistakes == 1:
				coutn += tot


print(coutn)
				