l = [s for s in open('input.txt').read().strip('\n\n').split('\n')]



maxCount = 0
count = 0



idx = []
for x in range(0, len(l)):
	try:
		if l[x].index('S'):
			idx.append(x)
			idx.append(l[x].index('S'))
	except:
		# do nothing
		maxCount = 0

# Start a queue of places to check
queue = []

queue.append([idx[0], idx[1] - 1])
queue.append([idx[0], idx[1] + 1])
queue.append([idx[0] - 1, idx[1]])
queue.append([idx[0] + 1, idx[1]])


def shift(x, current):
	match l[current[0]][current[1]]:
		case 'J':
			return [current[0] - 1, [current[1] - 1]]

def f(x):
	
	match l[x[0]][x[1]]:
		case 'J':
			count += 1
			return 
	
	# try left
	if x[0] > 0:
		 x = shift(-1, x)
		count += 1
		return count + f([a - 1 ,b])
		
	# try right
	x = shiftRight(x)
	if x[0] < len(l[x[0]]):
		x = shift(1, x)
		count += 1
		return count + f([a - 1 ,b])
		
	# try up
	x = shiftUp(x)
	if x[1] > 0:
		x = shift
		count += 1
		return count + f([a - 1 ,b])
		
	# try down
	x = shiftDown(x)
	if x[1] < len(l):
		count += 1
		return count + f([a - 1 ,b])
		
	
	

for i in queue:	# try the first in the queue
	# try left
	count = f(queue.pop())
	
	if (count > maxCount):
		maxCount = count
		
	count = 0
	
	
print(maxCount)