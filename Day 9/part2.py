# I forced myself to do this one on my own to ensure part 1 improved my recursion skills

# read in the values
l = [[int(s) for s in y.split(' ')] for y in open('input.txt').read().split('\n') if (y)]

# reverse the list
for i in range(0, len(l)):
	i = int(i)
	current = len(l[i]) - 1
	for x in range(0, 1 + (len(l[0]) // 2)):
		tmp = l[i][x]
		l[i][x] = l[i][current]
		l[i][current] = tmp
		current -= 1

def recursiveF(x):
	# check whether all values in x are 0
	coutn = 0
	for y in x:
		coutn += y
		# Break out of this loop
		if y > 0 or y < 0:
			break
	
	# All values are zero, return zero
	if coutn == 0:
		return 0
	
	# create the diff array
	diff = []
	for y in range(1, len(x)):
		diff.append(x[y] - x[y - 1])
	
	return x[-1] + recursiveF(diff)

print(sum(recursiveF(x) for x in l))