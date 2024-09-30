#include <iostream>
#include <functional>
#include <vector>

using ll = long long;
using namespace std;

int main () {
  int n, m;
  cin >> n >> m;
  vector<vector<int>> adj (n);
  vector<ll> cost (n, 0),
             parent (n, -1),
             outdegree (n, 0),
             depth (n, 0),
             roots,
             leaves;

  // read costs  
  for (auto& c : cost) cin >> c;

  // connect tree
  for (int i = 0; i < m; ++i) {
    int from, to;
    cin >> from >> to;
    from--; to--;
    adj[from].push_back(to);
    parent[to] = from;
    outdegree[from]++;
  }

  // determine parents and leaves
  for (int i = 0; i < n; ++i) {
    if (parent[i]==-1) roots.push_back(i);
    if (outdegree[i]==0) leaves.push_back(i);
  }

  // pass down cost and depth through the tree
  // a "treefix sum", if you will...
  function<void(int)> pass_down_from = [&] (int parent) {
    for (auto child : adj[parent]) {
      cost[child] += cost[parent];
      depth[child] = depth[parent]+1;
      pass_down_from(child);
    }
  };

  for (auto root : roots) { pass_down_from(root); }
  
  // determine the cost of the lowest common ancestor of nodes a and b
  function<ll(int,int)> lca_cost = [&] (int a, int b) {
    while (depth[a] < depth[b]) { b = parent[b]; }  
    while (depth[b] < depth[a]) { a = parent[a]; }
    while (a != b && a != -1 && b != -1) {
      a = parent[a];
      b = parent[b];
    }
    if (a == -1) return 0LL;
    return cost[a];
  };

  ll minCost = cost[leaves[0]] + cost[leaves[1]];
  
  for (int i = 0; i < leaves.size(); ++i) {
    for (int j = i+1; j < leaves.size(); ++j) {
      int a = leaves[i], b = leaves[j];
      ll costAB = cost[a] + cost[b] - lca_cost(a,b);
      minCost = min(minCost, costAB);
    }
  }
  
  cout << minCost << '\n';
}