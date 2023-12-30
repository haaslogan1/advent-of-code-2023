# Idea:
# Traverse through each hand and rank -> create an array with hand and corresponding rank
# Iterate through each hand adding the hand to the corresponding hands array
# Sort each hands array
# Calculate sum of rank * index of each hand

import re

# checking for five of a kind
def isFive(hand):
	hand = sorted(list(hand))
	aCount = len([i for i in hand if i == 'A'])
	return hand[0] == hand[4] \
	or (hand[1] == hand[4] and aCount == 1) \
	or (hand[2] == hand[4] and aCount == 2) \
	or (hand[3] == hand[4] and aCount == 3) \
	or aCount == 4

# checking for four of a kind
def isFour(hand):
	hand = sorted(list(hand))
	aCount = len([i for i in hand if i == 'A'])
	return aCount == 3 \
	or (aCount == 2 and (hand[2] == hand[3] or hand[3] == hand[4] or hand[2] == hand[4])) \
	or (aCount == 1 and (hand[1] == hand[3] or hand[2] == hand[4])) \
	or hand[0] == hand[3] or hand[1] == hand[4]
	
# checking for full house
def isfullH(hand):
	hand = sorted(list(hand))
	aCount = len([i for i in hand if i == 'A'])
	return (hand[0] == hand[1] and hand[2] == hand[4]) or (hand[0] == hand[2] and hand[3] == hand[4]) \
	or (aCount == 1 and hand[1] == hand[2] and hand[3] == hand[4])
	
# checking for three of a kind
def isThreeKind(hand):
	hand = sorted(list(hand))
	aCount = len([i for i in hand if i == 'A'])
	bCount =len([i for i in hand if i == hand[1]])
	return hand[0] == hand[2] or hand[1] == hand[3] or hand[2] == hand[4] \
	or (aCount == 1 and (hand[2] == hand[3] or hand[1] == hand[2] or hand[3] == hand[4])) \
	or aCount == 2
		
# checking for two pair
def isTwoPair(hand):
	hand = sorted(list(hand))
	return (hand[0] == hand[1] and hand[2] == hand[3]) \
	or (hand[1] == hand[2] and hand[3] == hand[4]) \
	or (hand[0] == hand[1] and hand[3] == hand[4])
	
# checking for one pair
def isOnePair(hand):
	hand = sorted(list(hand))
	aCount = len([i for i in hand if i == 'A'])
	return hand[0] == hand[1] or hand[2] == hand[3] \
	 or hand[1] == hand[2] or hand[3] == hand[4] \
	 or aCount > 0

def sort(hand):
	# Sort each hands array
	for i in range(0, len(hand)):
		hand[i][0] = list(hand[i][0])
		for j in range(0,5):
			match hand[i][0][j]:
				case 'A':
					hand[i][0][j] = 'N'
				case 'K':
					hand[i][0][j] = 'M'
				case 'Q':
					hand[i][0][j] = 'K'
				case 'J':
					hand[i][0][j] = 'A'
				case 'T':
					hand[i][0][j] = 'J'
				case '9':
					hand[i][0][j] = 'I'
				case '8':
					hand[i][0][j] = 'H'
				case '7':
					hand[i][0][j] = 'G'
				case '6':
					hand[i][0][j] = 'F'
				case '5':
					hand[i][0][j] = 'E'
				case '4':
					hand[i][0][j] = 'D'
				case '3':
					hand[i][0][j] = 'C'
				case '2':
					hand[i][0][j] = 'B'
				case '1':
					hand[i][0][j] = 'A'
	return hand

# Traverse through each hand and rank -> create an array containing all hands and corresponding rank
hands = []
with open('input.txt') as content:
	for cont in content:
		hands.append(re.findall(r'[\dQJTKA]+', cont))

# Create each array
highCard = []
onePair = []
twoPair = []
threeKind = []
fullH = []
four = []
five = []

hands = sort(hands)

# Iterate through each hand adding the hand to the corresponding hands array
for hand in hands:
	ha = hand[0]

	# Is this hand five of a kind?
	if isFive(ha):
		five.append(hand)
		continue
	
	# Is this hand four of a kind?
	if isFour(ha):
		four.append(hand)
		continue
	
	# Is full house?
	if isfullH(ha):
		fullH.append(hand)
		continue
	
	# three of a kind?
	if isThreeKind(ha):
		threeKind.append(hand)
		continue

	if isTwoPair(ha):
		twoPair.append(hand)
		continue
		
	if isOnePair(ha):
		onePair.append(hand)
		continue

	highCard.append(hand)
	
# Count up the total value
coutn = 0
idx = 1
print(sorted(threeKind))
for i in sorted(highCard):
	coutn += (idx * int(i[1]))
	idx += 1

for i in sorted(onePair):
	coutn += (idx * int(i[1]))
	idx += 1
	
for i in sorted(twoPair):
	coutn += (idx * int(i[1]))
	idx += 1
	
for i in sorted(threeKind):
	coutn += (idx * int(i[1]))
	idx += 1

for i in sorted(fullH):
	coutn += (idx * int(i[1]))
	idx += 1
	
for i in sorted(four):
	coutn += (idx * int(i[1]))
	idx += 1

for i in sorted(five):
	coutn += (idx * int(i[1]))
	idx += 1

print(coutn)