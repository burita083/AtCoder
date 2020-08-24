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
    ll n;
    cin >> n;
    vector<pair<ll,ll> >v;
    rep(i, 0, n) {
        ll x, l; cin >> x >> l;
        v.push_back(make_pair(x+l, x-l));
    }
    sort(v.begin(), v.end());
    ll mn = -INF; 
    ll ans = 0;
    rep(i, 0, n) {
        ll r = v[i].first;
        ll l = v[i].second;
        if (mn <= l) {
            mn = r;
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}