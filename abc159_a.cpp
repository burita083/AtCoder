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
using ll = long long;
 
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
  int N, M;
  cin >> N >> M;
  if (N <= 1 && M <= 1) {
      cout << 0 << endl;
    return 0;
  } else if (N <= 1 && M >= 2) {
    auto ans = ncr(M, 2);
    cout << ans.x << endl;
    return 0;

  } else if (N >= 2 && M <= 1) {
    auto ans = ncr(N, 2);
    cout << ans.x << endl;
    return 0;

  } else {
    auto ans = ncr(N, 2) + ncr(M, 2);
    cout << ans.x << endl;
    return 0;

  }
}
