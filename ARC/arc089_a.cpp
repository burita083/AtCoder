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
    int nx = 0;
    int ny = 0;
    int time = 0;
    int count = 0;
    rep(i, 0, N) {
        int t, x, y; 
        cin >> t >> x >> y;
        time = t-time;
        nx = x-nx;
        ny = y-ny;
        if (time >= nx+ny) {
            if ( (time % 2 == 0 && (nx+ny) % 2 == 0) || (time % 2 != 0 && (nx+ny) % 2 != 0)  )  {
                ++count;
            } else {
                cout << "No" << endl;
                return 0;
            }
        } else {
            cout << "No" << endl;
            return 0;
        }
    }
    
    if (count == N) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}