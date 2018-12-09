def doReact(a, b):
	return (a.lower() == b and b.upper() == a) or (a.upper() == b and b.lower() == a)  

def minimizePolymer(polymer):
	i = 0
	while(i < len(polymer) - 1):
		if doReact(polymer[i], polymer[i+1]):
			string1 = "" if i - 1 < 0 else polymer[:i]
			string2 = "" if i + 2 > len(polymer) else polymer[i+2:]
			polymer = string1 + string2
			if i != 0:
				i -= 1	
		else:
			i+=1

	return len(polymer)	

inputFile = open('input.txt')
polymer = inputFile.readline()
print minimizePolymer(polymer)