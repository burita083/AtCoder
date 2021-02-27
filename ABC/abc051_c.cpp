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
    int sx, sy, tx, ty;
    cin >> sx >> sy >> tx >> ty;
    int dx = tx - sx, dy = ty - sy;
    string res = "";
    rep(i, 0, dx) res += "R";
    rep(i, 0, dy) res += "U";
    rep(i, 0, dx) res += "L";
    rep(i, 0, dy) res += "D";

    res += "D";
    rep(i, 0, dx+1) res += "R";
    rep(i, 0, dy+1) res += "U";
    res += "L";
    res += "U";
    rep(i, 0, dx+1) res += "L";
    rep(i, 0, dy+1) res += "D";
    res += "R";
    cout << res << endl;
    return 0;
}