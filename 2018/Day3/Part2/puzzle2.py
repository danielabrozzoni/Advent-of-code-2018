import re
inputFile = open("input.txt")
matrixDimension = 1000
matrix = [[0]*matrixDimension for i in range(matrixDimension)]
lines = inputFile.readlines()
claimed = [False for i in range(len(lines) + 1)];

for line in lines: 
	line = re.split('[#@:\n]', line.replace(" ", ""))[1:4];
	id = int(line[0])
	position = 	re.split(',', line[1])
	dimension = re.split('x', line[2])

	for j in range (int(position[0]), int(dimension[0]) + int(position[0])):
		for i in range(int(position[1]), int(dimension[1]) + int(position[1])):
			if(matrix[i][j] != 0):
				claimed[matrix[i][j]] = True
				claimed[id] = True
			else:
				matrix[i][j] = id;

for i in range(1, len(claimed)): 
	if claimed[i] == False:
		print i
