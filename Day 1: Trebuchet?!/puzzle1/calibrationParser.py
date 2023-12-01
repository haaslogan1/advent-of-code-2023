import re

def parseNumbers(data):
	
	# Value that we need to know!
	# Sum of each first and last digit from each line
	calibrationVal = 0
	
	# Step through each string in the data array
	for i in data:
		
		# Export an array of ints in the line
		arr = re.findall(r'\d', i)
		
		# Get the two digit sum
		total = (int(arr[0]) * 10) + int(arr[len(arr) - 1])
		
		# Add to the calibration value
		calibrationVal += total
		
	return calibrationVal


def main():
	
	
	# Open the calibration input file 
	calibrationDoc = open('inputCalibration.txt', 'r')
	
	# Parse the calibration input file to a 2-d array
	data = calibrationDoc.readlines()
	
	# close the open file object
	calibrationDoc.close()
	
	# parseNumbers for a sum
	print(parseNumbers(data))
	
	# a = 'a1b2c3'
# 	
# 	print(re.search('[0-9]+', a).group())
	

if __name__ == "__main__":
	main()