#include <bits/stdc++.h>
using namespace std;


int main() {
    int n, s, m, tmp, curr, counter = 0;
    cin >> n >> s >> m;
    int a = n;
    vector<int> nums;
    vector<bool> visited;
    while(a--) {
        cin >> tmp;
        nums.push_back(tmp);
        visited.push_back(false);
    }
    curr = s - 1;
    while(true) {
        // cout << curr << " " << n << endl;
        if(nums[curr] == m) {
            cout << "magic" << endl;
            cout << counter;
            break;
        }
        else if(curr < 0) {
            cout << "left" << endl;
            cout << counter;
            break;
        }
        else if(curr >= n) {
            cout << "right" << endl;
            cout << counter;
            break;
        }
        if(visited[curr]) { //square already visited, loop
            cout << "cycle" << endl;
            cout << counter;
            break;
        }
        else { //square not visited
            visited[curr] = true;
            curr += nums[curr];
        }
        counter++;
        
        
    }
}