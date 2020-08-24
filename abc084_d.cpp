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
    if (n == 1) return false;

    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) { 
              return false;
         }
    }
    return true;
}

int main() {
    int Q;
    cin >> Q;
    vi a(Q);
    pair<int, bool> dp[101000];
    pair<int, bool> p = make_pair(INF, false);
    fill(dp, dp+101000, p);
    rep(i, 0, Q) {
        int res = 0;
        int l, r;
        cin >> l >> r;
        rep(k, l, r+1) {
            if (k % 2 != 0) {
               if (dp[k].first != INF) {
                   if (dp[k].second) {
                       ++res;
                   }
                   continue;
               }

               if (is_prime(k)) {
                    int nk = (k+1)*0.5;
                    if (dp[nk].first != INF) {
                        if (dp[nk].second) {
                            ++res;
                        }
                        continue;
                    }
                   if (is_prime((k+1)*0.5)) {
                       ++res;
                       dp[k].first = 0;
                       dp[k].second = true;
                   } else {
                       dp[k].first = 0;
                       dp[k].second = false;
                   }
               } else {
                       dp[k].first = 0;
                       dp[k].second = false;
               }
            }
        }
        cout << res << endl;
    }
    return 0;
}
