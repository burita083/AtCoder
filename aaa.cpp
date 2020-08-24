#include <vector>
#include <math.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <deque>
#include <map>
using namespace std;
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
 
const int mod = 1000000007;
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
  for (int i = 0; i < k; i++) a *= n - i;
  for (int i = 1; i <= k; i++) b *= i;
  return a / b;
}
 
int main() {
  ll n, a, b;
  cin >> n >> a >> b;
  ll bunbo = a;
  ll bunshi = 1;
  rep(i, 0, a) {
      bunshi *= (a-i) % MOD;
  }
  ll aa = bunshi/bunbo;

  bunbo = b;
  bunshi = 1;
  rep(i, 0, b) {
      bunshi *= (b-i) % MOD;
  }
  ll bb = bunshi/bunbo;
  ll ans = (ll(pow(2, n)) % MOD) - (aa%MOD) - (bb%MOD) - 1;
  cout << ans << endl;
  return 0;
}