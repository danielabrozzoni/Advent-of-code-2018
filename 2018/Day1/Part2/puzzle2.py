from sets import Set

inputFile = open('input.txt')
seenFrequencies = Set([0])
currentFrequency = 0;

while True: 
	for line in inputFile:
		currentFrequency += (int) (line)
		if currentFrequency in seenFrequencies: 
			print currentFrequency
			exit(0)
		seenFrequencies.add(currentFrequency)
	inputFile.seek(0)