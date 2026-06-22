#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {

  ll in;
  cin >> in;
  ll sum;
  while(1) {
    sum = 0;
    while(in) {
      sum += in%10;
      in/=10;
    }
    if(sum < 10) break;
    in=sum;
  }
  cout << sum << endl;

}