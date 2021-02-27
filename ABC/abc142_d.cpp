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
map<int, int> ans;
void f(int n) {
    for (int i = 2; i * i <= n; i++) {
        if (n % i != 0) continue;
        while (n % i == 0) {
            n /= i;
            ans[i]++;
        }
    }
    if (n != 1) ans[n]++;
}

// Greatest Common Divisor 最大公約数
ll gcd(ll a, ll b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

// least common multiple 最小公倍数
ll lcm(ll a, ll b) {
    ll g = gcd(a, b);
    return a / g * b;
}

// 公約数列挙 O(√n)
vector<ll> commonDivisor(ll a, ll b){
    ll n = gcd(a, b);
    vector<ll> res;
    for(ll i = 1; i * i <= n; i++){
        if(n % i == 0){
            res.push_back(i);
            if(i != n / i) res.push_back(n / i);
        }
    }
    return res;
}

// 約数列挙 O(√n)
vector<ll> divisor(ll n){
    vector<ll> res;
    for(ll i = 1; i * i <= n; i++){
        if(n % i == 0){
            res.push_back(i);
            if(i != n / i) res.push_back(n / i);
        }
    }
    sort(res.begin(), res.end());
    return res;
}

map<ll, ll> prime_factor(ll n) {
    map<ll, ll> res;
    for (ll i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            ++res[i];
            n /= i;
        }
    }
    if (n != 1) res[n] = 1;
    return res;
}

int coprime(ll a, ll b) {
  return (gcd(a, b) == 1);
}

int main() {
    ll A, B;
    cin >> A >> B;
    ll g = gcd(A, B);
    map<ll, ll> res = prime_factor(g);
    cout << res.size() + 1 << endl;
    return 0;
}