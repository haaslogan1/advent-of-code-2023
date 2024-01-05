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

	for y in range(1, len(tst)):
		y = int(y)
		if (y > (len(tst) / 2)):
			print(tst[y:int(len(tst))])
			print(tst[int((2 * (y - (int(len(tst)) / 2)))):y])
			if (str(tst[y:int(len(tst))])[::-1] == str(tst[int((2 * (y - (int(len(tst)) / 2)))):y])):
				tot = y
				for z in x:
					print(z[y:len(tst)])
					print(z[int((2 * (y - (len(tst) / 2)))):y])
					if (str(z[y:len(tst)])[::-1] != str(z[int((2 * (y - (len(tst) / 2)))):y])):
						tot = 0
						break
				coutn += tot
		elif (y <= (len(tst) / 2)):
			if(str(tst[0:y])[::-1] == str(tst[y:(y * 2)])):
				tot = y
				for z in x:
					if(str(z[0:y])[::-1] != str(z[y:(y * 2)])):
						tot = 0
						break
				coutn += tot
		
		print()
		
		
# 		print(tst[0:num])
# 		try:
# 			if (tst[0:num] == tst[num:(2*num)]):
# 				print(tst[0:num])
# 				lineCnt = num
# 				for y in x:
# 					if (y[0:num] != y[num:(2*num)]):
# 						lineCnt = 0
# 						break
# 				
# 				coutn += lineCnt
# 					
# 		except: pass
# 		
# 		try:
# 			if(tst[(len(tst) - 1 - num):num] == tst[((len(tst) - 1 - num) * 2):(num / 2)]):
# 				print(tst[(len(tst) - 1 - num):num])
# 				lineCnt = num - (len(tst) - 1 - num)
# 				for y in x:
# 					if (y[(len(y) - 1 - num):num] != y[((len(y) - 1 - num) * 2):(num / 2)]):
# 						lineCnt = 0
# 						break
# 				
# 				coutn += lineCnt
# 				
# 		except: pass
# 		print()

print(coutn)
				