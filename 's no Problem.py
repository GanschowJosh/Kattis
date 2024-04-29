import sys
from heapq import *
from collections import defaultdict

def prim(graph, start_node):
    mst = defaultdict(set)
    visited = set()
    edges = [
        (cost, to, start_node)
        for to, cost in graph[start_node].items()
    ]
    heapify(edges)

    while edges:
        cost, frm, to = heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost2 in graph[to].items():
                if to_next not in visited:
                    heappush(edges, (cost2, to, to_next))

    return mst

def main():
    n = int(input())
    graph = defaultdict(dict)
    for _ in range(n - 1):
        a, b, d = map(int, input().split())
        graph[a][b] = d
        graph[b][a] = d

    mst = prim(graph, 1)
    total_distance = sum(
        graph[frm][to]
        for frm in mst
        for to in mst[frm]
    )
    print(total_distance)


main()
