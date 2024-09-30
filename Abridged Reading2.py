from collections import defaultdict
import sys

sys.setrecursionlimit(2000)

def main():
    n, m = map(int, input().split())
    pages = list(map(int, input().split()))
    
    adj = defaultdict(list)
    parent = [-1] * n
    outdegree = [0] * n
    roots = []
    leaves = []

    # Build the graph
    for _ in range(m):
        from_chap, to_chap = map(int, input().split())
        from_chap -= 1  # Convert to 0-based index
        to_chap -= 1    # Convert to 0-based index
        adj[from_chap].append(to_chap)
        parent[to_chap] = from_chap
        outdegree[from_chap] += 1

    # Identify roots and leaves
    for i in range(n):
        if parent[i] == -1:
            roots.append(i)
        if outdegree[i] == 0:
            leaves.append(i)

    # Initialize cost and depth arrays
    cost = pages[:]
    depth = [0] * n

    # Pass down cost and depth through the tree
    def pass_down_from(node):
        for child in adj[node]:
            cost[child] += cost[node]
            depth[child] = depth[node] + 1
            pass_down_from(child)

    # Calculate depths and costs starting from roots
    for root in roots:
        pass_down_from(root)

    # Calculate the cost of the lowest common ancestor of nodes a and b
    def lca_cost(a, b):
        # Adjust depths to be the same
        while depth[a] < depth[b]:
            b = parent[b]
        while depth[b] < depth[a]:
            a = parent[a]
        
        # Move up until we find the LCA
        while a != b and a != -1 and b != -1:
            a = parent[a]
            b = parent[b]
        
        # If a is -1, return 0 since there's no valid ancestor
        if a == -1:
            return 0
        return cost[a]

    # Calculate the minimum cost for pairs of leaves
    min_cost = float('inf')

    for i in range(len(leaves)):
        for j in range(i + 1, len(leaves)):
            a = leaves[i]
            b = leaves[j]
            cost_ab = cost[a] + cost[b] - lca_cost(a, b)
            min_cost = min(min_cost, cost_ab)

    print(min_cost)

if __name__ == "__main__":
    main()
