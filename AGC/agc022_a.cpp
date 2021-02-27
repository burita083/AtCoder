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
    cin >> s;
    int len = s.length();
    vector<char> a;
    a.push_back('a');
    a.push_back('b');
    a.push_back('c');
    a.push_back('d');
    a.push_back('e');
    a.push_back('f');
    a.push_back('g');
    a.push_back('h');
    a.push_back('i');
    a.push_back('j');
    a.push_back('k');
    a.push_back('l');
    a.push_back('m');
    a.push_back('n');
    a.push_back('o');
    a.push_back('p');
    a.push_back('q');
    a.push_back('r');
    a.push_back('s');
    a.push_back('t');
    a.push_back('u');
    a.push_back('v');
    a.push_back('w');
    a.push_back('x');
    a.push_back('y');
    a.push_back('z');
    if (len < 26) {
        rep(i, 0, len) {
            a.erase(remove(a.begin(), a.end(), s[i]), a.end());
        }
        s.push_back(a.front());
    } else {
    }
    cout << s << endl;
    return 0;
}