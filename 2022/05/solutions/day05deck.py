from time import time
import sys
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.data
    
    def flip(self):
        if self.next != None:
            _tempNode = self.prev
            self.prev = self.next
            self.next = _tempNode
            self.prev.flip()
    def flipReverse(self):
        if self.prev != None:
            _tempNode = self.next
            self.next = self.prev
            self.prev = _tempNode
            return self.next.flipReverse()
        else:
            _tempNode = self.next
            self.next = self.prev
            self.prev = _tempNode
            return self

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def append(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    def popLeft(self):
        _tempNode = self.head
        self.head = self.head.next
        return _tempNode
    def blastLeft(self,amount):
        impactPoint = self.head
        for _ in range(1,int(amount)):
            impactPoint = impactPoint.next
        self.head = impactPoint.next
        if self.head != None:
            self.head.prev = None
        impactPoint.next = None
        return impactPoint
    def appendLeft(self,node):
        _tempnode = self.head
        self.head = node
        self.head.next = _tempnode
    def integrateLeft(self,start,end):
        if self.head == None:
            pass
        _tempNode = self.head
        self.head = start
        self.head.prev = None
        end.next = _tempNode
        if end.next != None:
            end.next.prev = end


def ParseGridInput(grid):
    grid = grid.split("\n")
    stackCount = int(grid.pop().strip().split(" ").pop())
    stackHeight = len(grid)
    stacks = []
    y = 1
    for _ in range(0, stackCount):
        stack = LinkedList()
        for j in range(0, stackHeight):
            char = grid[j][y]
            if char != ' ':
                stack.append(Node(grid[j][y]))
        y += 4
        stacks.append(stack)
    return stacks


def part1(path):
    with open(path) as f:
        data = f.read()
    grid, instrs = data.split("\n\n")
    stacks = ParseGridInput(grid)

    instrs = instrs.strip().split("\n")
    for line in instrs:
        # move 3 from 2 to 5
        _, amount, _, src, _, dest = line.strip().split(" ")
        impactNode = stacks[int(src)-1].blastLeft(amount)
        lastnode = impactNode.flipReverse()
        stacks[int(dest)-1].integrateLeft(impactNode,lastnode)
    # calc answer:
    s = ''
    for x in range(0, len(stacks)):
        s = s + stacks[x].popLeft().data
    return s




# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/05/inputs/aoc_2022_day05_large_input.txt"))
    print("### part 1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    #print('part 2:', part2("2022/05/inputs/aoc_2022_day05_large_input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
