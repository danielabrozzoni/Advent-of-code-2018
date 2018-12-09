def doReact(a, b):
	return (a.lower() == b and b.upper() == a) or (a.upper() == b and b.lower() == a)  

def minimizePolymer(polymer, bannedLetter):
	bannedLetter = bannedLetter.lower()
	i = 0
	while(i < len(polymer)):
		if polymer[i] == bannedLetter or polymer[i] == bannedLetter.upper():
			string1 = "" if i - 1 < 0 else polymer[:i]
			string2 = "" if i + 1 > len(polymer) else polymer[i+1:]
			polymer = string1 + string2
			if i != 0:
				i -= 1	

		if i < len(polymer) - 1 and doReact(polymer[i], polymer[i+1]):
			string1 = "" if i - 1 < 0 else polymer[:i]
			string2 = "" if i + 2 > len(polymer) else polymer[i+2:]
			polymer = string1 + string2
			if i != 0:
				i -= 1	
		else:
			i+=1
		#print polymer
	return len(polymer)	


inputFile = open('input.txt')
polymer = inputFile.readline()
minLenght = len(polymer)
for char in range(ord('a'), ord('z') + 1):
	minLenght = min(minLenght, minimizePolymer(polymer, chr(char)))
print minLenght