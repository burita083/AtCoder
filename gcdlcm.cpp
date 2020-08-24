#include <vector>
#include <math.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <deque>

typedef long long ll;
#define rep(i, a, n) for(int i = a; i<n; i++)
#define ALL(a) begin(a), end(a)
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
vector<int> vec;
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

// 3つ以上の最大公約数
ll gcd_n(vector<ll> &numbers) {
	ll l;
    l = numbers[0];

	for (int i = 1; i < numbers.size(); i++) {
        l = gcd(l, numbers[i]);
	}
	return l;
}

vector<ll> divisor(ll n){
    vector<ll> res;
    for(ll i = 1; i * i <= n; i++){
        if(n % i == 0){
            res.push_back(i);
            if(i != n / i) res.push_back(n / i);
        }
    }
    sort (res.begin(), res.end());
    return res;
}

int main() {
    string s;
    ll N;
    cin >> N;
    vector<ll> a(N);
    vector<ll> d = divisor(14);
    rep(i, 0, d.size()) {
        cout << d[i] << endl;
    }
    return 0;
}