inputFile = open('input.txt')

counter_2 = 0
counter_3 = 0

for line in inputFile:
	letters = {}
	for letter in line: 
		if letter in letters:
			letters[letter] += 1
		else:
			letters[letter] = 1

	for letter in letters: 
		if letters[letter] == 2:
			counter_2 += 1
			break

	for letter in letters: 
		if letters[letter] == 3:
			counter_3 += 1
			break

print counter_2 * counter_3