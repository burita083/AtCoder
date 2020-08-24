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

int main() {
    ll N, M;
    cin >> N >> M;

    vector<pair<ll, string> > a(M);
    vector<pair<bool, ll> > dp(N);
    dp[0].first = false;
    dp[0].second = 0;

    rep(i, 1, N+1) {
        dp[i].first = false;
    }

    for (ll i = 0; i < M; ++i) {
        cin >> a[i].first;
        cin >> a[i].second;
    }

    ll AC = 0;
    ll WA = 0;
    rep(i, 0, M) {
        if (dp[a[i].first].first == false) {
            if (a[i].second == "WA") {
                dp[a[i].first].second += 1;
            } else {
                ++AC;
                dp[a[i].first].first = true;
            }
        }
    }

    rep(i, 1, N+1) {
        if (dp[i].first) {
            WA += dp[i].second;
        }
    }

    cout << AC << endl;
    cout << WA << endl;
    return 0;
}