def fillMatrix(coordinates, matrix):
	x = int(coordinates[0])
	y = int(coordinates[1])
	
	for line in range(0, len(matrix)):
		for cell in range(0, len(matrix[line])):
			distance = abs(int(coordinates[0]) - line) + abs(int(coordinates[1]) - cell) 
			matrix[line][cell] += distance

def defineResult(matrix, treshold):
	result = 0
	for line in matrix:
		for cell in line:
			if cell < treshold:
				result += 1
	return result
 
def main():
	matrixDimension = 400
	matrix = [[0]*matrixDimension for i in range(matrixDimension)]

	inputFile = open('input.txt')
	for line in inputFile:
		coordinates = line[:-1].split(',')
		fillMatrix(coordinates, matrix)
	
	print defineResult(matrix, 10000)

main()