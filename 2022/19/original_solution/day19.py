from time import time
from collections import deque

class Blueprint:
    costOreRobot = 0
    costClayRobot = 0
    costObsRobot = [0,0]
    costGeodeRobot = [0,0]
    def __init__(self,ore,clay,obs,geode):
        self.costOreRobot = ore
        self.costClayRobot = clay
        self.costObsRobot = obs
        self.costGeodeRobot = geode

def calcGeodeMinute(amountOre,amountClay,amountobs,amountGeode,minute):
    global gBlueprint
    if minute > 24:
        return amountGeode
    else:

    pass

def part1(path):
    with open(path) as f:
        lines =f.readlines()
    blueprints = []
    for line in lines:
        ore,clay,obs,geode = line.split(". ")
        ore = int(ore.split(" ")[6])
        clay = int(clay.split(" ")[4])
        obs = obs.split(" ")
        obs = [int(obs[4]),int(obs[7])]
        geode = geode.split(" ")
        geode = [int(geode[4]),int(geode[7])]
        blueprints.append(Blueprint(ore,clay,obs,geode))
    
    for bp in blueprints:
        global gBlueprint
        gBlueprint = bp
    return 0


def part2(path):
    with open(path) as f:
        lines =f.readlines()
    pass
    
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/19/inputs/example.txt"))
    #print('part 2:')
    #part2("2022/19/inputs/input.txt")
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
