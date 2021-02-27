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
 
const ll mod = 1000000007;
struct mint {
  ll x;
  mint(ll x = 0) : x((x % mod + mod) % mod) {}
  mint operator-() const { return mint(-x); }
  mint& operator+=(const mint a) {
    if ((x += a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator-=(const mint a) {
    if ((x += mod - a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator*=(const mint a) {
    (x *= a.x) %= mod;
    return *this;
  }
  mint operator+(const mint a) const {
    mint res(*this);
    return res += a;
  }
  mint operator-(const mint a) const {
    mint res(*this);
    return res -= a;
  }
  mint operator*(const mint a) const {
    mint res(*this);
    return res *= a;
  }
  mint pow(ll t) const {
    if (!t) return 1;
    mint a = pow(t >> 1);
    a *= a;
    if (t & 1) a *= *this;
    return a;
  }
 
  // for prime mod
  mint inv() const { return pow(mod - 2); }
  mint& operator/=(const mint a) { return (*this) *= a.inv(); }
  mint operator/(const mint a) const {
    mint res(*this);
    return res /= a;
  }
};
 
mint ncr(ll n, ll k) {
  mint a = 1, b = 1;
  for (ll i = 0; i < k; i++) a *= n - i;
  for (ll i = 1; i <= k; i++) b *= i;
  return a / b;
}
 
int main() {
    ll N;
    cin >> N;
    vl a(N);
    map<ll, ll> mp;
    rep(i, 0, N) {
        cin >> a[i];
        mp[a[i]]++;
    }
    //ll dp[3000000];
    //fill(dp, dp+3000000, -1);
            ll b = 2;
    ll res = 0;
        for(auto x : mp) {
            auto ans = ncr(x.second, b);
            //dp[x.second] = ans.x;
            res += ans.x;
        }


    rep(i, 0, N) {
        ll temp = res;
        ll m = mp[a[i]];
        mp[a[i]]--;
                //if (dp[m] != -1) {
                //    temp -= dp[m];
                //} else {
                    auto ans = ncr(m, b);
                    temp -= ans.x;
                //}

                //if (dp[mp[a[i]]] != -1) {
                //    temp += dp[mp[a[i]]];
                //} else {
                    ans = ncr(mp[a[i]], b);
                //    dp[mp[a[i]]] = ans.x;
                    temp += ans.x;
                //}
        cout << temp << endl;
        mp[a[i]]++;
    }
    return 0;
}
