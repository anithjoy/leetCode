import heapq

def dijkstra(graph, source):
    # Initialization
    distance = {vertex:float("infinity") for vertex in graph}
    distance[source] = 0
    priority_queue = [(0,source)]

    while priority_queue:
        # Extract vertex with minimum distance
        currDistance, currNode = heapq.heappop(priority_queue)

        # Relaxation
        for vertex,weight in graph[currNode].items():
            newDistance = currDistance + weight

            if newDistance < distance[vertex]:
                distance[vertex] = newDistance
                heapq.heappush(priority_queue, (newDistance,vertex))

    return distance


# Example usage:
graph_example = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

source_vertex = 'A'
result_distances = dijkstra(graph_example, source_vertex)

print(f"Shortest distances from {source_vertex}: {result_distances}")
