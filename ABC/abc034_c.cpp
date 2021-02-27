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
 
// nCrはO(k)で求まる
mint ncr(ll n, ll k) {
  mint a = 1, b = 1;
  for (int i = 0; i < k; i++) a *= n - i;
  for (int i = 1; i <= k; i++) b *= i;
  return a / b;
}
 
int main() {
  ll W, H;
  cin >> W >> H;
  // 二項係数の和をもし知らなくても、制約みて間に合わそう、だからいい方法ないかな？という考え方を身につける。
  auto ans = ncr(W+H-2, W-1);
  cout << ans.x << endl;
  return 0;
}
