import networkx as nx

g = nx.Graph()
n, q = list(map(int, input().split()))
g.add_nodes_from(i for i in range(1, n+1))
for _ in range(n+1):
    u, v = map(int, input().split())
    g.add_edge(u, v)
for _ in range(q):
    u, v = map(int, input().split())
    paths = list(nx.all_simple_paths(g, u, v))
    print(len(paths))