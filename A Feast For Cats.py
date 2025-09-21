from math import comb
from array import array

INF = 10**9

T = int(input())
for _ in range(T):
    M, C = map(int, input().split())

    # Early prune: still must consume input
    pairs = comb(C, 2)

    # Build symmetric distance matrix using 2-byte unsigned shorts (D_ij ≤ 3000)
    mat = [array('H', [0]) * C for _ in range(C)]
    for _ in range(pairs):
        i, j, d = map(int, input().split())
        mat[i][j] = d
        mat[j][i] = d

    if M < C:
        print("no")
        continue

    # Prim's MST in O(C^2)
    in_mst = [False] * C
    key = [INF] * C
    key[0] = 0
    mst_sum = 0

    for _ in range(C):
        u = -1
        best = INF
        # pick next vertex
        for v in range(C):
            kv = key[v]
            if not in_mst[v] and kv < best:
                best = kv
                u = v
        in_mst[u] = True
        mst_sum += best

        row = mat[u]
        for v in range(C):
            if not in_mst[v]:
                w = row[v]
                if w and w < key[v]:
                    key[v] = w

    need = C + mst_sum
    print("yes" if M >= need else "no")
