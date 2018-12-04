import re
import datetime
import operator


class Shift:
	def __init__(self, time, description):
		self.time = time
		self.description = description

	def __lt__(self, other):
		return self.time < other.time

	def __repr__(self):
		return str(self.__class__) + ": " + str(self.__dict__) + "\n"

def createShifts():
	shifts = []
	inputFile = open("input.txt")
	for line in inputFile: 
		line = re.split(']', line[1:-1])
		shifts.append(Shift(datetime.datetime.strptime(line[0], '%Y-%m-%d %H:%M'), line[1][1:]))

	shifts.sort()
	return shifts

def defineSleepyGuard(shifts):
	
	currentGuard = 0
	lastAsleepTime = 0
	guards = {}

	for shift in shifts:
		if re.match(r'Guard (.*) begins shift', shift.description):
			currentGuard = int(re.findall(r'\b\d+\b', shift.description)[0])
		elif shift.description == "falls asleep":
			lastAsleepTime = shift.time
		else:
			diff = shift.time - lastAsleepTime
			asleepMinutes = (diff.days * 24 * 60) + (diff.seconds/60)
			if currentGuard in guards:
				guards[currentGuard] += asleepMinutes
			else:
				guards[currentGuard] = asleepMinutes 

	return max(guards.iteritems(), key=operator.itemgetter(1))[0]

def defineSleepyMinute(shifts, sleepyGuard):
	
	currentGuard = 0
	lastAsleepTime = 0
	minutes = {}

	for shift in shifts:
		if shift.description == "Guard #" + str(sleepyGuard) + " begins shift":
			currentGuard = sleepyGuard
		elif re.match(r'Guard (.*) begins shift', shift.description):
			currentGuard = -1
		elif currentGuard == -1:
			continue
		elif shift.description == "falls asleep":
			lastAsleepTime = shift.time
		else:
			currentDate = lastAsleepTime
			endDate = shift.time
			delta = datetime.timedelta(minutes=1)
			while currentDate < endDate:
				timeStamp = str(currentDate.hour) + ":" + str(currentDate.minute)
				if timeStamp in minutes:
					minutes[timeStamp] += 1
				else: 
					minutes[timeStamp] = 1
				currentDate += delta

	return max(minutes.iteritems(), key=operator.itemgetter(1))[0]	

def main():
	shifts = createShifts()	
	sleepyGuard = defineSleepyGuard(shifts)
	sleepyMinute = defineSleepyMinute(shifts, sleepyGuard)
	print sleepyGuard * int(sleepyMinute[2:])
main()