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

// 各桁の和を計算する関数
int findSumOfDigits(int n) {
  int sum = 0;
  while (n > 0) { // n が 0 になるまで
    sum += n % 10;
    n /= 10;
  }
  return sum;
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

//想定解答との絶対誤差または相対誤差が 10−6以下の場合+1以上だしておく。適当に15とかでもおｋ．
//cout << fixed << setprecision(15);

int main() {
    string s;
    ll N;
    cin >> N;
    vector<vector<ll> > a(3, vector<ll>(N));
    rep(i, 0, 3) {
        rep(j, 0, N) {
            cin >> a[i][j];
        }
    }
    rep(i, 0, 3) {
        sort(a[i].begin(), a[i].end());
    }
    ll res = 0;
    rep(i, 0, N) {
        auto Iter1 = lower_bound(a[0].begin(), a[0].end(), a[1][i]);
        auto start1 = Iter1 - a[0].begin();
        auto Iter2 = upper_bound(a[2].begin(), a[2].end(), a[1][i]);
        auto end2 = a[2].end() - Iter2;
        ll a = start1 * end2;
        res += a;
    }
    cout << res << endl;
    return 0;
}