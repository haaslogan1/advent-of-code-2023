l = ["O....#....",\
"O.OO#....#",
".....##...",
"OO.#O....O",
".O.....O#.",
"O.#..O.#.#",
"..O..#O..O",
".......O..",\
"#....###..",\
"#OO..#...."]

# open the file as a list of each row
# l = open('input.txt').read().strip('\n\n').split('\n')

import re


# shift all rocks up
# traverse from the bottom of the list to the top
for y in range(0, len(l[0])):
	# traverse through each character of the row
	for x in range(1, len(l)):
	
		# check for the possibility to move up
		if  list(l[x])[y] == 'O' and list(l[x - 1])[y] == '.':
			
			idx = x
			
			while idx > -1:
				if list(l[idx - 1])[y] != '.':
					break
			
				print(str(y) + ' ' + str(x))
				print(l[idx - 1])
				print(l[idx])
				print()
				tmp1 = list(l[idx])
				tmp1[y] = '.'
			
				tmp2 = list(l[idx - 1])
				tmp2[y - 1] = 'O'
				
			
				l[idx] = ''.join(tmp1)
				l[idx - 1] = ''.join(tmp2)
				
				print(l[idx - 1])
				print(l[idx])
				print()
				print()
				
				idx -= 1


for x in l:
	print(x)

# current iteration value
itera = len(l)

# current count 
coutn = 0

# iterate through each value
for r in l:
	
	# x is the list of all 0s in the current row
	x = re.findall(r"O", r)
	
	# add to the total count
	coutn += (len(x) * itera)
	
	# decrease the iteration value
	itera -= 1
	
# print total count
print(coutn)