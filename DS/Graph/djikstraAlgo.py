import heapq

def dijkstra(graph, source):
    # Initialization
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        # Extract vertex with minimum distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Relaxation
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

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
