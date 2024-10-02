#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 10005;
const int LOG = 14; // Enough for n <= 10^4

vector<int> adj[MAXN];
int parent[MAXN][LOG];
int depth[MAXN];
int n;

// DFS to set up the parent array and depth
void dfs(int v, int p, int d) {
    parent[v][0] = p;
    depth[v] = d;

    for (int neighbor : adj[v]) {
        if (neighbor != p) {
            dfs(neighbor, v, d + 1);
        }
    }
}

// Prepare the parent table for LCA
void preprocess() {
    for (int j = 1; j < LOG; j++) {
        for (int i = 1; i <= n; i++) {
            if (parent[i][j - 1] != -1) {
                parent[i][j] = parent[parent[i][j - 1]][j - 1];
            }
        }
    }
}

// Find LCA of u and v
int lca(int u, int v) {
    if (depth[u] < depth[v]) {
        swap(u, v);
    }

    // Bring u and v to the same depth
    for (int j = LOG - 1; j >= 0; j--) {
        if (depth[parent[u][j]] >= depth[v]) {
            u = parent[u][j];
        }
    }

    if (u == v) return u;

    for (int j = LOG - 1; j >= 0; j--) {
        if (parent[u][j] != parent[v][j]) {
            u = parent[u][j];
            v = parent[v][j];
        }
    }

    return parent[u][0];
}

// Count paths between u and v
int countPaths(int u, int v) {
    int lca_node = lca(u, v);
    return (depth[u] + depth[v] - 2 * depth[lca_node]) + 1; // Number of paths from u to v
}

int main() {
    int q;

    cin >> n >> q;

    // Initialize parent array
    for (int i = 1; i <= n; i++) {
        fill(parent[i], parent[i] + LOG, -1);
    }

    // Read edges (n + 1 edges)
    for (int i = 0; i < n + 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Start DFS from node 1 (assuming 1 is the root)
    dfs(1, -1, 0);
    preprocess();

    // Answering queries
    for (int i = 0; i < q; i++) {
        int u, v;
        cin >> u >> v;
        cout << countPaths(u, v) << endl;
    }

    return 0;
}
