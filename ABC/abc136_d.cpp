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
    string S;
    cin >> S;
    vector<int> group(S.length());
    int g = 0;
    int r = 0;
    int l = 0;
    vector<int> res;
    bool first = true;
    bool second = false;
    int next_r = 0;
    int r_i = 0;
    int l_i = 0;
    rep(i, 0, S.length()) {
        if(S[i] == 'R' && S[i+1] == 'L') {
            if (l_i != 0) {
                r++;
                l++;
                cout << r_i;
                cout << "番目 R ";
                cout << l_i;
                cout << "番目 Lでrとlは" << endl;

                cout << r;
                cout << "と";
                cout << l;
                cout << "個";
                if ((r+l) % 2 == 0) {
                    res[r_i] = ((r+l)/2);
                    res[l_i] = ((r+l)/2);
                } else {
                    if (r % 2 == 0) {
                        res[r_i] = ((r+l)/2);
                        res[l_i] = ((r+l)/2+1);
                    } else {
                        res[r_i] = ((r+l)/2+1);
                        res[l_i] = ((r+l)/2);
                    }
                }
                r = 0;
                l = 0;
                r_i = i;
                l_i = i+1;
                i++;
                cout << endl;
                res.push_back(0);
                res.push_back(0);

            } else {
                r_i = i;
                l_i = i+1;
                res.push_back(0);
                res.push_back(0);
                i++;
            }
        } else if (S[i] == 'R') {
            ++r;
            res.push_back(0);
        } else {
            ++l;
            res.push_back(0);
        }
    }
    rep(i, 0, res.size()) {
        cout << res[i];
        cout << " ";
    }
        cout << endl;
    return 0;
}