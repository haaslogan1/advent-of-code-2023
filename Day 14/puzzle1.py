l = ["OOOO.#.O..",\
"OO..#....#",\
"OO..O##..O",\
"O..#.OO...",\
"........#.",\
"..#....#.#",\
"..O..#.O.O",\
"..O.......",\
"#....###..",\
"#....#...."]

import re


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