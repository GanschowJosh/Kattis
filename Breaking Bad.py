from collections import defaultdict

def build_graph(items, suspicious_pairs):
    graph = defaultdict(list)
    for pair in suspicious_pairs:
        item1, item2 = pair.split()
        graph[item1].append(item2)
        graph[item2].append(item1)
    return graph

def dfs(graph, start, visited, walter_items, jesse_items):
    visited[start] = True
    walter_items.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, jesse_items, walter_items)

def divide_items(items, suspicious_pairs):
    graph = build_graph(items, suspicious_pairs)
    visited = {item: False for item in items}
    walter_items, jesse_items = [], []
    
    for item in items:
        if not visited[item]:
            dfs(graph, item, visited, walter_items, jesse_items)
    
    return walter_items, jesse_items

def main():
    N = int(input())
    items = [input().strip() for _ in range(N)]
    M = int(input())
    suspicious_pairs = [input().strip() for _ in range(M)]
    
    walter_items, jesse_items = divide_items(items, suspicious_pairs)
    
    if len(walter_items) == 0 or len(jesse_items) == 0:
        print("impossible")
    else:
        print(" ".join(walter_items))
        print(" ".join(jesse_items))

if __name__ == "__main__":
    main()
