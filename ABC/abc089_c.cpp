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
    int N;
    cin >> N;
    vl a(N);
    map<char, ll> mp;
    ll numbers = 0;
    int kinds = 0;
    rep(i, 0, N) {
        string s;
        cin >> s;
        if (s[0] == 'M' || s[0] == 'A' || s[0] == 'R' || s[0] == 'C' || s[0] == 'H') {
            mp[s[0]]++;
            numbers++;
        }
    }
    ll two = 0;
    for(auto x: mp) {
        if (x.second >= 2) {
            ++two;
        }
        kinds++;
    }
    ll one = kinds - two;
    ll res = (numbers * (numbers-1) * (numbers-2)) / 6;
    ll b = (one * (one-1)) / 2;
    if (kinds >= 3) {
        for(auto x: mp) {
            if (x.second >= 2) {
                res = x.second * b;
            }
        }
        if (one>=3) {
            res += (one * (one-1) * (one-2))/6;
        }

        if (two == 2) {
            x.second * x.second * one;
        }

        if (two == 3) {
            x.second * x.second * one;
            3C1 * 
            3C2
            3C3
        }

        if (two == 4) {
            4C1
            4C2
            4C3
        }

        if (two == 5) {
            5C1
            5C2
            5C3
        }
    } else {
        cout << 0 << endl;
        return 0;
    }
    cout << res << endl;
    return 0;
}