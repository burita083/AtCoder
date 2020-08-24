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
    string s;
    int N;
    cin >> N;
    //vector<vector<int>> data(3, vector<int>(4));
    //初期値0
    //vector<int> data(i, 0);
    int a = 15*N;
    int b = 100*(N/10);
    int res;
    if (N <= 6) {
        cout << a << endl;
        return 0;
    } else if (N <= 10) {
        cout << 100 << endl;
        return 0;
    } else if (N <= 20) {
        int n = N%10;
        res = 15*n + 100 * (N/10);
        if (res > 200) res = 200;
    } else if (N <= 30) {
        int n = N%10;
        res = 15*n + 100 * (N/10);
        if (res > 300) res = 300;
    } else if (N <= 40) {
        int n = N%10;
        res = 15*n + 100 * (N/10);
        if (res > 400) res = 400;
    } else {
        int n = N%10;
        res = 15*n + 100 * (N/10);
        if (res > 500) res = 500;

    }
    cout << res << endl;
    return 0;
}