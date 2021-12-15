from collections import defaultdict
from queue import PriorityQueue

# graph class that implements dijkstra's algorithm
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def __init__(self, map):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

        for i in range(len(map) * len(map[0])):
            self.addNode(i)

        for i in range(len(map)):
            for j in range(len(map[0])):
                if i > 0:
                    self.addEdge(i * len(map[0]) + j, (i - 1) * len(map[0]) + j, map[i - 1][j])
                if j > 0:
                    self.addEdge(i * len(map[0]) + j, i * len(map[0]) + j - 1, map[i][j - 1])
                if i < len(map) - 1:
                    self.addEdge(i * len(map[0]) + j, (i + 1) * len(map[0]) + j, map[i + 1][j])
                if j < len(map[0]) - 1:
                    self.addEdge(i * len(map[0]) + j, i * len(map[0]) + j + 1, map[i][j + 1])

    def addNode(self,value):
        self.nodes.add(value)
    
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

    def dijkstra(self, inital):
        D = {v:float('inf') for v in range(len(self.nodes))}
        D[inital] = 0

        visited = set()

        pq = PriorityQueue()
        pq.put((0, inital))

        while not pq.empty():
            (dist, v) = pq.get()
            visited.add(v)

            for edge in self.edges[v]:
                weight = dist + self.distances[(v, edge)]

                if edge not in visited:
                    oldcost = D[edge]
                    newcost = weight

                    if oldcost > newcost:
                        D[edge] = newcost
                        pq.put((newcost, edge))     
        return D

