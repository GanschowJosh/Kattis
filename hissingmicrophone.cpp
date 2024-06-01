#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
    string a;
    cin >> a;
    for(int i = 0; i < a.length(); i++) {
        if(a[i] == 's' && a[i] == a[i+1]) {
            cout << "hiss" << endl;
            return 0;
        }
    }
    cout << "no hiss" << endl;
    return 0;
}