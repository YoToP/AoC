from time import time
from collections import defaultdict
from copy import copy,deepcopy

class Node:
    def __init__(self, data):
        self.nodes = []
        self.data = data
        self.stepsToEnd = 1e7
    
    def __repr__(self):
        return f'Node("{self.data}","{self.nodes})'

    def addNode(self,node):
        self.nodes.append(node)

    def validateNodes(self):
        for node in self.nodes:
            delta = node.data - self.data
            if delta > 1 or delta < 0:
                self.nodes.remove(node)
        for node in self.nodes:
            node.validateNodes()

    def calcStepsToEnd(self,steps):
        if steps < self.stepsToEnd:
            self.stepsToEnd = steps
            for node in self.nodes:
                node.calcStepsToEnd(steps+1)



        


def part1(path):
    with open(path) as f:
        lines = f.readlines()
    matrix = []
    height = 0
    width = 0
    endI = 0
    endJ = 0
    for line in lines: # load playing field into matrix
        height += 1
        line = line.replace('\n', '')
        width = len(line)
        lstLine = []
        for nr in line:
            if nr == 'S':
                lstLine.append(0)
            elif nr == 'E':
                endI = height-1
                lstLine.append(-1)
                endJ = len(lstLine)
            else:
                lstLine.append(ord((nr))-ord('a')+1)
        matrix.append(lstLine)
    copymatrix = deepcopy(matrix)
    head = Node(0)
    nodeList = dict()
    i = 0 #height
    j = 0 #width
    lastRowFirstNode = head
    currentNode = head
    for i in range(0,height):
        for j in range(0,width):
            if i == 0:
                if j == 0:
                    matrix[i][j] = head
                else:
                    newNode = Node(matrix[i][j])
                    matrix[i][j-1].addNode(newNode)
                    matrix[i][j] = newNode
            else:
                if j == 0:
                    newNode = Node(matrix[i][j])
                    matrix[i-1][j].addNode(newNode)
                    matrix[i][j] = newNode
                else:
                    if matrix[i][j] == 9:
                        pass
                    newNode = Node(matrix[i][j])
                    matrix[i][j-1].addNode(newNode)
                    matrix[i-1][j].addNode(newNode)
                    matrix[i][j] = newNode
    head.validateNodes()
    
    head.calcStepsToEnd(0)
    
        
    return matrix[endI][endJ].stepsToEnd

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    p1time = start_time
    path = "2022/12/inputs/example.txt"
    print("part 1:",part1(path))
    print("### run time p1 is %s miliseconds" % (int(round(time() * 1000)) - p1time))
    p2time = int(round(time() * 1000))
    #print("part 2:",solvep2("2022/12/inputs/input.txt",5))
    print("### run time p1 is %s miliseconds" % (int(round(time() * 1000)) - p2time))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))