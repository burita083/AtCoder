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
int main() {
    int N, Q; cin >> N >> Q;
    string S;
    cin >> S;
    vi l(Q), r(Q);
    rep(i, 0, Q) {
        cin >> l[i] >> r[i];
    }

    vi a(N);
    rep(i, 0, N){
        if (S[i] == 'A' && S[i+1] == 'C') a[i] = 1;
    }
    vi sum(N+1);
    rep(i, 0, N) {
        sum[i+1] = sum[i] + a[i];
    }

    rep(i, 0, Q) {
        cout << sum[r[i] - 1] - sum[l[i]- 1] << endl;
    }
    return 0;
}