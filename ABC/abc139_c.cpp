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
int main() {
    string s;
    int N;
    cin >> N;
    //vector<vector<int>> data(3, vector<int>(4));
    //初期値0
    //vector<int> data(i, 0);
    vl a(N);
    rep(i, 0, N) {
        cin >> a[i];
    }
    ll res = 0;
    ll mx = 0;
    rep(i, 0, N-1) {
        if (a[i] >= a[i+1]) {
            ++mx;
            if (i+1 == N-1) {
                res = max(mx, res);
            }
        } else {
            res = max(mx, res);
            mx = 0;
        }
    }
    cout << res << endl;
    return 0;
}