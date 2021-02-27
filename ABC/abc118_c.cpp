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
    ll N;
    cin >> N;
    vl a(N);
    rep(i, 0, N) {
        cin >> a[i];
    }
    ll ans = INF;
    rep(i, 0, N-1) {
        ll ans1 = a[i];
        ll ans2 = a[i+1];
        while(true) {
            ll a = max(ans1, ans2);
            ll b = min(ans1, ans2);
            ans1 = a % b;
            ans2 = b;

            if (a % b == 0) {
                ans = min(b, ans);
                break;
            }
        }
    }
    cout << ans << endl;
    return 0;
}