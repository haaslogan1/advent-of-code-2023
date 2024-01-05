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
		
		# check for two lines that are the same
		if (x[num] == x[num - 1]):
			
			#initialize the above line count
			lineCount = num
		
			# initialize the idx
			smallNum = num - 2
			num += 1
			
			# while we are still in the range of the list
			while smallNum > -1 and num < len(x):
				# check if two lines are not equivalent
				if (x[smallNum] != x[num]):
					# since the lines aren't equivalent, this finding will not count to
					# the total
					lineCount = 0
					break
				else:
					# since the lines are equivalent, iterate and proceed
					num += 1
					smallNum -= 1
			
			# add to the counter
			coutn += (100 * lineCount)
			
	
	# Check for vertical lines
	tst = x[0]

	# Iterate through each possible vertical line (len of the string - 1)
	for y in range(1, len(tst)):
		
		# if the vertical line will be in the second half of the string
		if (y > (len(tst) / 2)):
			# split the second half of the string by the amt of chars on each side
			if (str(tst[y:int(len(tst))])[::-1] == str(tst[int((2 * (y - (int(len(tst)) / 2)))):y])):
				# save y as a temp num used to add to the total count
				tot = y
				# iterate through each string in the complete list to see if it also matches like the first line
				for z in x:
					if (str(z[y:len(tst)])[::-1] != str(z[int((2 * (y - (len(tst) / 2)))):y])):
						tot = 0
						break
				coutn += tot
		elif (y <= (len(tst) / 2)):
			# split the first half of the string (or total string) by the amt of chars on each side
			if(str(tst[0:y])[::-1] == str(tst[y:(y * 2)])):
				# save y as a temp num used to add to the total count
				tot = y
				# iterate through each x in y
				for z in x:
					if(str(z[0:y])[::-1] != str(z[y:(y * 2)])):
						tot = 0
						break
				coutn += tot


print(coutn)
				