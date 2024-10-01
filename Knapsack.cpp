#include <bits/stdc++.h>
#include <vector>
#include <algorithm>

using namespace std;

pair<int, vector<int>> knapsack(int capacity, int n, const vector<int>& values, const vector<int>& weights) {
    vector<vector<int>> dp(n+1, vector<int>(capacity + 1, 0));

    for(int i = 1; i <= n; i++) {
        for(int w = 1; w <= capacity; w++) {
            if (weights[i-1] <= w) dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w]);
            else dp[i][w] = dp[i-1][w];
        }
    }

    vector<int> chosen;

    int w = capacity;
    for(int i = n; i > 0; i--) {
        if(dp[i][w] != dp[i-1][w]) {
            chosen.push_back(i-1);
            w -= weights[i-1];
        }
    }
    reverse(chosen.begin(), chosen.end());
    return {chosen.size(), chosen};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int c, n;
    while (cin >> c >> n) {
        vector<int> values(n), weights(n);

        for(int i = 0; i < n; i++){
            cin >> values[i] >> weights[i];
        }

        auto [numchosen, chosen] = knapsack(c, n, values, weights);

        cout << numchosen << "\n";

        for(int i = 0; i < numchosen; i++) {
            cout << chosen[i] << (i < numchosen - 1 ? " " : "\n");
        }
    }

    return 0;
};