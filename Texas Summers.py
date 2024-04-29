import heapq
import math

def calculate_distance(point1, point2, sun_exposure):
    distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    return distance * math.exp(sun_exposure)

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_nodes

def shortest_path(previous_nodes, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()
    return path

n = int(input())
shady_spots = [tuple(map(int, input().split())) for _ in range(n)]
dormitory = tuple(map(int, input().split()))
classroom = tuple(map(int, input().split()))

points = shady_spots + [dormitory, classroom]
sun_exposure = 5
graph = {i: {j: calculate_distance(points[i], points[j], sun_exposure) for j in range(len(points)) if i != j} for i in range(len(points))}

distances, previous_nodes = dijkstra(graph, len(points) - 2)
path = shortest_path(previous_nodes, len(points) - 2, len(points) - 1)

# Convert the indices back to shady spot indices and adjust for 1-indexing
path = [i+1 if i < len(shady_spots) else ('D' if i == len(shady_spots) else 'C') for i in path]

print(path)
