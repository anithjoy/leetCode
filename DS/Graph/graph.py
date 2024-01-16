#  lets build graph data structure. 
# Simple implementation of graph data structure using dictionary 
#  There are two ways to store a graph:
# 1. Adjacency Matrix
# 2. Adjacency List
# Approach - Adjancency List
"""
1. Create dictionary
2. add Vertex()
3. add edges():
    1. add vertex of start and end vertex
    2. then i am going to add edges by using start vertex as a key and end vertex as a value
4. delete vertex():
    1. removing all the vertex from edges 
    2. remove vertex from dictionary
"""
class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def addVertex (self, vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = []

    def addEdges (self, start, end):
        self.addVertex(start)
        self. addVertex(end)
        self.graph[start].append(end)
        self.graph[end].append(start)

    def deleteVertex (self, vertex):
        # removing all the vertex from edges
        for node in self.graph[vertex]:
            if vertex in self.graph[node]:
                self.graph[node].remove(vertex)
        # removing vertex
        del self.graph[vertex]


    
# Example Usage:
my_graph = Graph()

my_graph.addEdges('A', 'B')
my_graph.addEdges('A', 'C')
my_graph.addEdges('B', 'D')
my_graph.addEdges('C', 'D')
my_graph.addEdges('C','E')
my_graph.addEdges('C','F')
my_graph.addEdges('F','X')

