#include <stdio.h>

int modulo_solitaire(int m, int n, int k, int pairs[][2]) {
    // Create an array of length m+1 and initialize all elements to 0
    int dp[m+1];
    for (int i = 0; i <= m; i++) {
        dp[i] = 0;
    }
    
    // Iterate over the pairs and update the dp array
    for (int i = 0; i < n; i++) {
        int a = pairs[i][0];
        int b = pairs[i][1];
        for (int j = 0; j <= m; j++) {
            if (dp[j] == i) {
                dp[(j + a) % m] = i + 1;
                dp[(j + b) % m] = i + 1;
            }
        }
    }
    
    // Return the minimum number of moves required to win the game
    return dp[k];
}

int main() {
    int m, n, k;
    scanf("%d %d %d", &m, &n, &k);
    int pairs[n][2];
    
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &pairs[i][0], &pairs[i][1]);
    }
    
    printf("%d\n", modulo_solitaire(m, n, k, pairs));
    
    return 0;
}
