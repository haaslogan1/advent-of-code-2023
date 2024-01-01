# Needed to improve my recursion skills:
# https://www.reddit.com/r/adventofcode/comments/18e5ytd/comment/kclk5nv/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

# Get the array of ints
l = [[int(i) for i in s.split()] for s in open('input.txt').read().split('\n') if s.strip()]



def n(l):	
	# check if all values in l are zero
	# if true, reutrn 0 and continue
	if sum(i != 0 for i in l) == 0:
		return 0

	# append the difference to the m list
	m = []
	for i in range(len(l)-1):
		m.append(l[i+1]-l[i])
	
	# return difference array
	return l[-1] + n(m)

print(sum(n(i) for i in l))