import re
inputFile = open("input.txt")
matrixDimension = 2000
matrix = [[0]*matrixDimension for i in range(matrixDimension)]
claimed = 0;

for line in inputFile: 
	line = re.split('[#@:\n]', line.replace(" ", ""))[1:4];
	id = int(line[0])
	position = 	re.split(',', line[1])
	dimension = re.split('x', line[2])

	for j in range (int(position[0]), int(dimension[0]) + int(position[0])):
		for i in range(int(position[1]), int(dimension[1]) + int(position[1])):
			if(matrix[i][j] != 0 and matrix[i][j] != 'X'):
				claimed += 1
				matrix[i][j] = 'X';
			elif matrix[i][j] != 'X':
				matrix[i][j] = id;
print claimed