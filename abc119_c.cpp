#include <vector>
#include <math.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <deque>
#include <map>

typedef long long ll;
#define rep(i, a, n) for(int i = a; i<n; i++)
#define ALL(a) begin(a), end(a)
#define mii map<int, int>
#define msi map<string, int>
#define vi vector<int>
#define vl vector<ll>
#define MOD 1000000007
#define INF 1e9
using namespace std;
template<class T> inline bool chmin(T& a, T b) {
    if (a > b) {
        a = b;
        return true;
    }
    return false;
}
template<class T> inline bool chmax(T& a, T b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}

int N, A, B, C;
vi L(10);
int dfs(int i, int a, int b, int c) {
    if (i >= N) {
        if (min({a, b, c}) > 0) {
            return abs(a-A) + abs(b-B) + abs(c-C) - 30;
        } else {
            return INF;
        }
    }
    int ret0 = dfs(i+1, a, b, c);
    int ret1 = dfs(i+1, a+L[i], b, c) + 10;
    int ret2 = dfs(i+1, a, b+L[i], c) + 10;
    int ret3 = dfs(i+1, a, b, c+L[i]) + 10;
    return min({ret0, ret1, ret2, ret3});
}
int main() {
  cin >> N >> A >> B >> C; 
  rep(i, 0, N) {
      cin >> L[i];
  }
  cout << dfs(0, 0, 0, 0) << endl;
}