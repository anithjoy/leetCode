from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start, end):
        self.add_vertex(start)
        self.add_vertex(end)
        self.graph[start].append(end)
        self.graph[end].append(start)

    def display(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")


    def displayDFS(self, startNode):

        stack = []
        stack.append(startNode)
        visited = set()
        visited.add(startNode)

        while stack:
            
            node = stack.pop()
            print(node)

            for eachNode in self.graph[node]:
                if eachNode not in visited:
                    stack.append(eachNode)
                    visited.add(eachNode)


    def displayBFS(self, startNode):
        q = deque()
        q.append(startNode)
        visited = set()
        

        while q:
            node = q.popleft()
            visited.add(node)
            print(node)

            for eachNode in self.graph[node]:
                if eachNode not in visited:
                    q.append(eachNode)
                    


        





# Example Usage:
my_graph = Graph()

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')
my_graph.add_edge('C','E')
my_graph.add_edge('C','F')
my_graph.add_edge('F','X')

my_graph.display()
my_graph.displayDFS(startNode="A")

print()
my_graph.displayBFS(startNode="A")