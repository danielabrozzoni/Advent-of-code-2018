inputFile = open('input.txt')
currentFrequency = 0;

for line in inputFile:
	currentFrequency += (int) (line)

print currentFrequency