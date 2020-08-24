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
    int N, M;
    cin >> N >> M;
    vector<pair<int, int> > a(M);
    rep(i, 0, M) {
        int s, c;
        cin >> s >> c;
        pair<int, int> p = make_pair(s, c);
        a[i] = p;
    }

    string res = "100";

    bool one = false;
    bool two = false;
    bool three = false;
    int one_ = -1;
    int two_ = -1;
    int three_ = -1;
    if (N == 1) {
        res = "0";
        rep(i, 0, M) {
            if (!one) {
                    res.replace(0, 1, to_string(a[i].second));
                    one = true;
                    one_ = a[i].second;
            } else {
                    if (one_ != a[i].second) {
                        cout << -1 << endl;
                        return 0;
                    }
            }
        }

    } else {
        if (N == 2) {
            res = "10";
        } else if (N == 3) {
            res = "100";
        }
    rep(i, 0, M) {
        if (a[i].first == 1) {
            if (a[i].second == 0) {
                    cout << -1 << endl;
                    return 0;
            } else {
                if (!one) {
                    res.replace(0, 1, to_string(a[i].second));
                    one = true;
                    one_ = a[i].second;
                
                } else {
                    if (one_ != a[i].second) {
                        cout << -1 << endl;
                        return 0;
                    }
                }
            }
        } else if (a[i].first == 2) {
            if (!two) {
                res.replace(1, 1, to_string(a[i].second));
                two = true;
                two_ = a[i].second;
                
            } else {
                if (two_ != a[i].second) {
                    cout << -1 << endl;
                    return 0;
                }
            }
        } else {
            if (!three) {
                res.replace(2, 1, to_string(a[i].second));
                three = true;
                three_ = a[i].second;
            } else {
                if (three_ != a[i].second) {
                    cout << -1 << endl;
                    return 0;
                }
            }
        }
    }
    }
    cout << res << endl;
    return 0;
}