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
# define p(s) std::cout << s ;
# define pl(s)  std::cout << s << endl;
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
int gcd(ll a, ll b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
int main() {
    ll N; cin >> N;
    vi a(N);
    rep (i, 0, N) cin >> a[i];
    vi left(N+1, 0), right(N+1,0);
    rep(i, 0, N) left[i+1] = gcd(left[i], a[i]);
    for (int i = N-1; i >= 0; --i) right[i] = gcd(right[i+1], a[i]);

    int res = 0;
    rep(i, 0, N) {
        int l = left[i];
        int r = right[i+1];
        chmax(res, gcd(l, r));
    }

    cout << res << endl;
  
    return 0;
}