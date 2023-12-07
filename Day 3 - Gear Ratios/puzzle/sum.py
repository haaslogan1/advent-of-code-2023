import math as m, re

# Learning from https://topaz.github.io

# Open the board as an array of strings
board = list(open('../input'))

# Create the chars map to pinpoint the location of each special character
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

# for r and row iterate through board with an index
for r, row in enumerate(board):
    # Iterate through each number found in the row
    for n in re.finditer(r'\d+', row):
    	# Check what is above and below the number and left and right 
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}
		
		# append to a number to the special chars array if it is to a special char
        for o in edge & chars.keys():
            chars[o].append(int(n.group()))
            
# print the sum for puzzles 1 & 2
print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))