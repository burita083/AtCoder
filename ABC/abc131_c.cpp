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
int main() {
    ll A, B, C, D;
    cin >> A >> B >> C >> D;
    ll a = (B / C)-((A-1) / C);
    ll b = (B / D)-((A-1) / D);
    ll l = lcm(C, D);
    ll c = (B / l)-((A-1) / l);
    cout << (B - A + 1) - (a + b - c) << endl;
    return 0;
}