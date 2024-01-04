l = [['#.##..##.', '..#.##.#.', "##......#", "##......#", "..#.##.#.", "..##..##.", "#.#.##.#."],\
["#...##..#",\
"#....#..#",\
"..##..###",\
"#####.##.",\
"#####.##.",\
"..##..###",\
"#....#..#"]]

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
	
	# iterate through each index where there could be a line
	for num in range(1, len(tst)):
		try:
			if (tst[0:num] == tst[num:(2*num)]):
				lineCnt = num
				for y in x:
					if (y[0:num] != y[num:(2*num)]):
						lineCnt = 0
						break
				
				coutn += lineCnt
					
		except: pass
		
		try:
			if(tst[(len(tst) - 1 - num):num] == tst[((len(tst) - 1 - num) * 2):(num / 2)]):
				lineCnt = num - (len(tst) - 1 - num)
				for y in x:
					if (y[(len(y) - 1 - num):num] != y[((len(y) - 1 - num) * 2):(num / 2)]):
						lineCnt = 0
						break
				
				coutn += lineCnt
				
		except: pass

print(coutn)
				