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
int main() {
    int R, G, B, N;
    cin >> R >> G >> B >> N;
    vl a(N);
    int r_count = N/R;
    int g_count = N/G;
    int b_count = N/B;
    int res = 0;
    rep(r, 0, r_count+1) {
        int n = N;
        n -= R*r;
        if (n == 0) {
            ++res;
            continue;
        }
        rep(g, 0, g_count+1) {
            int temp = n;
            temp -= G*g;
            if (temp == 0) {
                ++res;
                continue;
            }
            if (temp > 0 && temp%B==0) {
                ++res;
                continue;
            }
        }
    }
    cout << res << endl;
    return 0;
}