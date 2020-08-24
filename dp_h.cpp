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
    int H, W;
    cin >> H >> W;
    vector<string> a(H+1);
    rep(i, 0, H) {
        cin >> a[i];
    }
    ll dp[H+1][W+1];
    rep(h, 0, H) {
        rep(w, 0, W) {
            dp[h][w] = -1;
            if (a[h][w] == '#') {
                dp[h][w] = 0;
            }
        }
    }
    rep(i, 0, H) {
        bool flag = false;
        if (a[0][i] == '#') {
            flag = true;
        }
        if (flag) {
            dp[0][i] = 0;
        }
    }

    rep(i, 0, W) {
        bool flag = false;
        if (a[i][0] == '#') {
            flag = true;
        }
        if (flag) {
            dp[i][0] = 0;
        }
    }
    dp[0][0] = 1;
    rep(h, 0, H) {
        rep(w, 0, W) {
            if (a[h][w] == '.') {
                if (w == 0 && h == 0) continue;
                ll res1 = 0;
                if (w-1 >= 0) {
                    res1 = dp[h][w-1];
                }

                ll res2 = 0;
                if (h-1 >= 0) {
                    res2 = dp[h-1][w];
                }
                if (h-1 >=0 || w-1 >= 0) {
                    dp[h][w] = (res1 + res2) % MOD;
                }
            }
        }
    }
    cout << dp[H-1][W-1] << endl;
    return 0;
}