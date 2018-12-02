def compareIDs(id_1, id_2):

	count = 0

	for i in range (0, len(id_1) - 1):
		if id_1[i] != id_2[i]:
			count += 1

	return count

def obtainEquals(id_1, id_2): 

	result = ""

	for i in range (0, len(id_1) - 1):
		if id_1[i] == id_2[i]:
			result += id_1[i]

	return result

def main(): 
	inputFile = open('input.txt')

	IDs = inputFile.readlines()

	for id_1 in IDs:
		for id_2 in IDs: 
			if compareIDs(id_1, id_2) == 1:
				print obtainEquals(id_1, id_2)
				exit(0)

main()