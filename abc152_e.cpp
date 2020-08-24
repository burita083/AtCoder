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

ll lcm_n(vector<ll> &numbers) {
	ll l;
	l = numbers[0];
	for (int i = 1; i < numbers.size(); i++) {
		l = lcm(l, numbers[i]);
	}
	return l;
}
long long modinv(long long a, long long m) {
    long long b = m, u = 1, v = 0;
    while (b) {
        long long t = a / b;
        a -= t * b; swap(a, b);
        u -= t * v; swap(u, v);
    }
    u %= m;
    if (u < 0) u += m;
    return u;
}
int main() {
    ll N;
    cin >> N;
    vl a(N);
    rep(i, 0, N) {
        cin >> a[i];
    }
    ll lc = 1;
    rep(i, 0, N) {
        lc = lcm(lc, a[i]);
    }

    ll res = 0;
    rep(i, 0, N) {
        //lc %= MOD;
        //ll ans = lc * modinv(a[i], MOD) % MOD;
        //res += ans;
        res += (lc / a[i]);
        res %= MOD;
    }
    //cout << res % MOD << endl;
    cout << res % MOD << endl;
    return 0;
}