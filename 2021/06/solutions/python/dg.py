from collections import defaultdict, Counter
from time import time
class ProblemA():
	#def setup(self):
	#	pass
	#def transform(self, vals):
	#	pass
	#def solveAll(self):
	#	pass
	
	spawntimer = 7
	newborntimer = 2
	days = 80
	
	def readFish(self, line):
		# Performance on 1048576 days: defaultdict(int) = 3.2s, Counter = 4.2s
		fish = defaultdict(int)
		fish |= Counter(map(int, line.split(",")))
		return fish
	
	def solveInstance(self, line):
		fish = self.readFish(line)
		
		for day in range(self.days):
			spawn = day + self.spawntimer
			newborn = spawn + self.newborntimer
			today = fish.pop(day, 0)
			fish[spawn] += today
			fish[newborn] = today # =: 3.2s, +=: 5.8s. lmao
		
		return sum(fish.values())

class ProblemB(ProblemA):
	days = 1048576



if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    with open("6/example1.txt") as f:
        lines = f.readlines()
    print(ProblemB().solveInstance(lines[0]))

    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))