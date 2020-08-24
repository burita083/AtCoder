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
    int N;
    cin >> N;
    //1<<nは2^n
    //2^nは全パターン数と一致
    //<<ビット(2進数)を左へシフトする
    //bit->0-7
    //2進数は先頭に0bをつけて表す
    int a[N];
    fill(a, a+N, -1);

    vector<vector<int> > b(N+1, vector<int>(N+1));

    rep(i, 1, N+1) {
        rep(j, 1, N+1) {
            b[i][j] = -1;
        }
    }
    rep(i, 1, N+1) {
        int A;
        cin >> A;
        rep(j, 0, A) {
            int x, y;
            cin >> x >> y;
            b[i][x] = y;
        }
    }
    rep(bit, 0, 1<<N) {
        vi S;
        vi F;
        rep(i, 0, N) {
            if (bit & (1<<i)) {
                    S.push_back(i+1);
                    //if(b[i][j] == 1) {
                    //    a[j] = 1;
                    //}
                //}
            } else {
                    F.push_back(i+1);
            }
        }
        cout << "正直者: {";
        rep(i, 0, S.size()) {
            cout << S[i] << " ";
        }
        cout << "} ";

        cout << "偽物: {";
        rep(i, 0, F.size()) {
            cout << F[i] << " ";
        }
        cout << "}" << endl;

        rep(i, 1, N+1) {
            rep(j, 1, N+1) {
                if (i == j) continue;
                cout << b[i][j];
                cout << " ";
            }
            cout << endl;
        }
    }
    //int res = 0;
    //rep (i, 0, N) {
    //    if (a[i] == 1) {
    //        ++res;
    //    }
    //}
    //cout << res << endl;

    return 0;
}