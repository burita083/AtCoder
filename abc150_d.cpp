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
// Greatest Common Divisor 最大公約数
int gcd(int x, int y) { return (x % y)? gcd(y, x % y): y; }
int lcm(int x, int y) { return x / gcd(x, y) * y; }
int main() {
  int n, M, a, b;
  cin >> n >> M;
  cin >> a;
  int i = 1;
  ll count = 0;
    for(int i = 1; i < n; ++i) {
        cin >> b;
        a = lcm(a, b);
    }
  while(1 <= i*(a/2) && i*(a/2) <= M) {
    if (i*(a/2) % 2 != 0) {
        ++count;
    }
    ++i;
  }
    cout << count << endl;
  
  return 0;
}