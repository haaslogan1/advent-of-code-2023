import re

if __name__ == "__main__":
	
	# Open Input parser
	data = open('input.txt', 'r')
	infile = data.readlines()
	
	# Start total count at 0
	coutn = 0
	
	# loop through each line of input
	for i in infile:
		# Only extract by the portion after the Card #. I don't care
		# about the card #.
		ignoreCard = i.split(':')
		
		# get the winning numbers and our numbers
		winning = re.findall(r'\d+', str(ignoreCard[1].split('|')[0]))
		myCards = re.findall(r'\d+', str(ignoreCard[1].split('|')[1]))
		
		# Total points earned this round
		thisRound = 0
		
		# Should I double the total or just start by adding 1?
		double = 0
		
		# Iterate through each winning number since it is less than my cards
		for win in winning:
			# If the number is in my cards, add to this rounds' points
			if win in myCards:
				# If we should double, multiply this round's total by 2. Otherwise, 
				# set this round's total to 1
				if double:
					thisRound *= 2
				else:
					thisRound = 1
					
					# Change the 'double' boolean to trye
					double = 1
					
				
				
		# add this round's score to the total
		coutn += thisRound
		
	print('Total: ' + str(coutn))
			
