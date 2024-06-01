#include <bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;

#define MEDIAN(a, b, c) ( (a>b) ? max(b, min(a, c)) : min(b, max(a, c))) //branchless median of three values

int main() {
    int n, t, temp, sum = 0, sumEven = 0;
    vector<int> a;
    vector<char> seq;
    cin >> n >> t;
    for(int i = 0; i < n; i++) {
        cin >> temp;
        a.push_back(temp);
        sum += temp;
        if (temp % 2 == 0) {
            sumEven += temp;
        }
        seq.push_back((char)((temp%26)+97));
    }
    switch (t) {
        case 1:
            cout << "7";
            return 0;
        case 2:
            if(a[0] > a[1]) {
                cout << "Bigger";
            }
            if(a[0] == a[1]) {
                cout << "Equal";
            }
            else {
                cout << "Smaller";
            }
            return 0;
        case 3:
            cout << MEDIAN(a[0], a[1], a[2]); 
            return 0;
        case 4:
            cout << sum;
            return 0;
        case 5:
            cout << sumEven;
            return 0;
        case 6:
            for (auto& it : seq) {
                cout << it;
            }
            return 0;
        case 7:
            int numcomps = 0;
            int ind = 0;
            while(true) {
                if(ind > n-1) {
                    cout << "Out";
                    return 0;
                }
                ind = a[ind];
                numcomps++;
                if(ind == n-1) {
                    cout << "Done";
                    return 0;
                }
                if(numcomps > n) {
                    cout << "Cyclic";
                    return 0;
                }
            }
    }
}