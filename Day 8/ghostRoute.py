# Needed performance help: https://www.reddit.com/r/adventofcode/comments/18df7px/comment/kf9t12b/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

from functools import reduce
from math import lcm

instruction, network = open('input.txt').read().split('\n\n')
network = network.split('\n')

# list of all the strings in this network
a=[i[0:3] for i in network]
# list of all the left points (going left from the string)
b=[i[7:10] for i in network]
# list of all the right points (going right from the string)
c=[i[12:15] for i in network]

# Remove the new line character from the end 
a.pop()

# starting points (end with A) - changed when iterating through
allnode=[i for i in a if i[2]=='A']
# set count to 0
count=0
# amount of strings ending in z
z=0
# list of all the count values
y=[]
# amount of strings that need to end in z
e=len(allnode)
# while we do not yet have all strings ending in 'Z'
while z<e:
	# iterate through all the LR instructions
    for direction in instruction:
    	# iterate through each char of the current str
        for i in range(len(allnode)): 
        	# if L, use the current index and choose the left-most string
            if direction == 'L':
                allnode[i] = b[a.index(allnode[i])]
            # if R, use the current index and choose the right-most string
            else:
                allnode[i] = c[a.index(allnode[i])]
        count+=1
        # check for 'Z' at the end of a string
        for x in allnode:
        	# if there is a z, we can add it to y and make the allnode list shorter
            if x[2]=='Z':
                z+=1
                allnode.remove(x)
                y.append(count)
print(reduce(lcm,y))