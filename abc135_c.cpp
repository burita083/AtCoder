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
    ll N;
    cin >> N;
    //vector<vector<int>> data(3, vector<int>(4));
    //初期値0
    //vector<int> data(i, 0);
    vl monsters(N+1);
    vl heros(N);
    ll res = 0;
    rep(i, 0, N+1) {
        cin >> monsters[i];
    }
    rep(i, 0, N) {
        cin >> heros[i];
    }
    rep(i, 0, N) {
        if (monsters[i] >= 1) {
            if (heros[i] >= monsters[i]) {
                res += monsters[i];
            } else {
                res += heros[i];
            }
            ll temp = monsters[i];
            monsters[i] -= heros[i];
            heros[i] -= temp;
            if (heros[i] <= 0) {
                continue;
            }
        }

        if (monsters[i+1] >= 1) {
            if (heros[i] >= monsters[i+1]) {
                res += monsters[i+1];
            } else {
                res += heros[i];
            }
            ll temp = monsters[i+1];
            monsters[i+1] -= heros[i];
            heros[i] -= temp;
        }
    }
        
    cout << res << endl;
    return 0;
}