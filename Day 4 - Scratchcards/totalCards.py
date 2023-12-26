import re

if __name__ == "__main__":
	
	# Open Input parser
	data = open('input.txt', 'r')
	infile = data.readlines()
	copyFile = infile
	
	# Start total count at 0
	arr = []
	
	# loop through each line of input to make the array the correct size
	# each index should contain 1 as we start with one of each card
	for i in infile:
		arr.extend([1])
	
	# Set the index to card 1 -> 0
	idx = 0
	
	# loop through each line of input
	for i in infile:
		
		currentIdx = idx
		
		# Only extract by the portion after the Card #. I don't care
		# about the card #.
		ignoreCard = i.split(':')
		
		# get the winning numbers and our numbers
		winning = re.findall(r'\d+', str(ignoreCard[1].split('|')[0]))
		myCards = re.findall(r'\d+', str(ignoreCard[1].split('|')[1]))

		
		
		# Iterate through each winning number since it is less than my cards
		for win in winning:

			# If the number is in my cards, add to the card array
			if win in myCards:
				# Add each iteration of this card to subsequent indeces
				try:
					arr[currentIdx + 1] += arr[idx]
				except:
					print('Index too large!')
				
				# Iterate to the next index
				currentIdx += 1
				
		# Move to the next index of arr
		idx += 1
		
	# total card count
	coutn = 0
	for x in arr:
		coutn += x
	
	print('Total: ' + str(coutn))
	