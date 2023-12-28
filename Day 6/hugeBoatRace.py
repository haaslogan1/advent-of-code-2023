import re

# Open the input file
content =  open('input.txt')



# Create the time and dist array
time = re.findall(r'\d+', content.readline().replace(' ', ''))
dist = re.findall(r'\d+', content.readline().replace(' ', ''))

print(time)
# Create the races array from the time and dist arrays
races = [[time[i], dist[i]] for i in range(0, len(time))]

# Set the counter
coutn = 1

for i in races:
	
	# Extract the time and dist
	time = int(i[0])
	dist = int(i[1])
	
	
	# Set the tmp counter
	tmpcoutn = 0
	
	# iterate through the range
	for x in range(1, time - 1):
		# Add a value if pressing the button for time x will beat the record
		if (x * (time - x) > dist):
			tmpcoutn += 1
	
	# Multiply by ways to win this race to get margin of error
	coutn *= tmpcoutn

# Print margin or error
print(coutn)