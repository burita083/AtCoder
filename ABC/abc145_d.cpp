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
#define rep(i, a, n) for(ll i = a; i<n; i++)
#define ALL(a) begin(a), end(a)
#define mii map<int, int>
#define msi map<string, int>
#define vi vector<int>
#define vl vector<ll>
#define MOD 1000000007
#define INF 1e9
#define showVector(v) rep(i,0,v.size()){p(v[i]);p(" ")} pl("")
#define p(s) std::cout << s ;
#define pl(s)  std::cout << s << endl;
using namespace std;

// 素数判定 O(√n)
bool is_prime(int n){
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) return false;
    }
    return true;
}

// 各桁の和を計算する関数
int findSumOfDigits(int n) {
  int sum = 0;
  while (n > 0) { // n が 0 になるまで
    sum += n % 10;
    n /= 10;
  }
  return sum;
}

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

//想定解答との絶対誤差または相対誤差が 10−6以下の場合+1以上だしておく。適当に15とかでもおｋ．
//cout << fixed << setprecision(15);

int main() {
    ll X, Y;
    cin >> X >> Y;
    vector<vector<ll> > dp(X+1, vector<ll>(Y+1));
    dp[0][0] = 1;
    dp[1][2] = 1;
    dp[2][1] = 1;
    rep(x, 0, X+1) {
        rep(y, 0, Y+1) {
            if (x == 0 && y == 0) continue;
            ll way1 = 0;
            ll way2 = 0;
            if (x-1>=0 && y-2 >= 0) {
                way1 = dp[x-1][y-2];
            }

            if (x-2 >= 0 && y-1>=0) {
                way2 = dp[x-2][y-1];
            }

            dp[x][y] = way1 + way2;
            dp[x][y] = dp[x][y] % MOD;
        }
    }
    cout << dp[X][Y] << endl;
    return 0;
}