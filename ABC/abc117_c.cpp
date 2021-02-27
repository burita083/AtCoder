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
    ll N, M;
    cin >> N >> M;
    vl a(M);
    vl b(M-1);
    rep(i, 0, M) {
        cin >> a[i];
    }

    int ans = 0;
    sort(a.begin(), a.end());
    
    if(N>=M) {
        cout << ans << endl;
        return 0;
    } else {
        rep(i, 0, M-1) {
            b[i] = abs(a[i+1]-a[i]);
        }
        sort(b.begin(), b.end());
        rep(i, 0, M-N) {
            ans += b[i];
        }
    }
    cout << ans << endl;
    return 0;
}