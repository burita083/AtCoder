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
    int N, M;
    cin >> N >> M;
    vector<vector<int> > s(M);
    rep(i, 0, M) {
        int k;
        cin >> k;
        rep(j, 0, k) {
            int a;
            cin >> a;
            --a;
            s[i].push_back(a);
        }
    }
    vector<int> p(M);
    rep(i, 0, M) {
        cin >> p[i];
    }
    ll res = 0;
    //1<<nは2^n
    //2^nは全パターン数と一致
    //<<ビット(2進数)を左へシフトする
    //bit->0-7
    //2進数は先頭に0bをつけて表す
    rep(bit, 0, 1<<N) {
        bool ok = true;
        rep(i, 0, M) {
            int on = 0;
            for (auto v: s[i]) {
                // ここを理解する
                cout << "bit ";
                cout << bit;
                cout << " ";
                // 左シフト、右シフトはきちんと括弧をつける。
                cout << (1<<v) << endl;
                if (bit & (1<<v)) {
                    ++on;
                }
            }
            // 条件、onになっているスイッチの個数を2で割った余りが一致するか。しないならば、flagをtrueにして、カウントしない
            if (on % 2 != p[i]) {
                ok = false;
            }
        }
        if (ok) ++res;
    }

    cout << res << endl;
    return 0;
}