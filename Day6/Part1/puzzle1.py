def fillMatrix(letter, coordinates, matrix):
	x = int(coordinates[0])
	y = int(coordinates[1])
	
	for line in range(0, len(matrix)):
		for cell in range(0, len(matrix[line])):
			distance = abs(int(coordinates[0]) - line) + abs(int(coordinates[1]) - cell) 
			if matrix[line][cell] == '0' or (int(matrix[line][cell][0]) != 0 and int(matrix[line][cell][:-1]) > distance):
				matrix[line][cell] = str(distance) + letter
			elif int(matrix[line][cell][0]) != 0 and int(matrix[line][cell][:-1]) == distance:
				matrix[line][cell] = str(distance) + '.'

def defineInfinite(matrix):
	infinite = []

	for cell in matrix[0]:
		if cell[-1] not in infinite:
			infinite.append(cell[-1])

	for cell in matrix[-1]:
		if cell[-1] not in infinite:
			infinite.append(cell[-1])
	for line in matrix:
		if line[0][-1] not in infinite:
			infinite.append(line[0][-1])

		if line[-1][-1] not in infinite:
			infinite.append(line[-1][-1])		
	return infinite

def countCells(matrix):
	count = {}
	for line in matrix:
		for cell in line:
			if(cell[-1] != '.'): 
				if cell[-1] not in count:
					count[cell[-1]] = 0
				count[cell[-1]] += 1

	return count

def defineResult(infinite, count):
	max = 0
	for letter in count:
		if count[letter] > max and letter not in infinite:
			max = count[letter]
	return max
 
def main(): 
	matrixDimension = 400
	matrix = [['0']*matrixDimension for i in range(matrixDimension)]

	inputFile = open('input.txt')
	letter = 'A'
	for line in inputFile:
		coordinates = line[:-1].split(',')
		matrix[int(coordinates[0])][int(coordinates[1])] = "0" + letter
		fillMatrix(letter, coordinates, matrix)
		letter = chr(ord(letter) + 1)

	print defineResult(defineInfinite(matrix), countCells(matrix))

main()