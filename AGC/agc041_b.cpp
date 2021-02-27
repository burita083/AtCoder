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
int main() {
    ll N, M, V, P;
    cin >> N >> M >> V >> P;
    vl a(N);
    rep(i, 0, N) {
        cin >> a[i];
    }
    //P問選ぶ
    // M人 × V問 
    // N問数
    vl answers();
    rep(i, 0, N) {
        a[i] += 2;
        rep(m, 0, M) {
            rep(v, 0, V) {
            }
        }
    }
    rep(i, 0, M) {
        rep(j, 0, V) {
        }
    }
    cout << N << endl;
    return 0;
}