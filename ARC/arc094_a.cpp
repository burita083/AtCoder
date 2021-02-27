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
    vi a(3);
    rep(i,0,3) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    int res = 0;
    ///ggg
    if (a[0]%2==0 && a[1]%2 == 0 && a[2]%2 ==0) {
        res = (a[2]-a[0])/2 + (a[2]-a[1])/2;
        cout << res << endl;
        return 0;
    } 

    //ggk
    if (a[0]%2==0 && a[1]%2 == 0 && a[2]%2 !=0) {
        a[1]++;
        a[0]++;
        res = (a[2]-a[0])/2 + (a[2]-a[1])/2;
        ++res;
        cout << res << endl;
        return 0;
    }

    //gkg
    if (a[0]%2==0 && a[1]%2 != 0 && a[2]%2 ==0) {
        a[2]++;
        a[0]++;
        res = (a[2]-a[0])/2 + (a[2]-a[1])/2;
        ++res;
        cout << res << endl;
        return 0;
    }

    //gkk
    if (a[0]%2==0 && a[1]%2 != 0 && a[2]%2 !=0) {
        a[2]++;
        a[1]++;
        res = (a[2]-a[0])/2 + (a[2]-a[1])/2;
        ++res;
        cout << res << endl;
        return 0;
    }

    //kgg
    if (a[0]%2!=0 && a[1]%2 == 0 && a[2]%2 ==0) {
        a[2]++;
        a[1]++;
        res = (a[2]-a[0])/2 + (a[2]-a[1])/2;
        ++res;
        cout << res << endl;
        return 0;
    }

    //kkg
    if (a[0]%2!=0 && a[1]%2 != 0 && a[2]%2 ==0) {
        a[0]++;
        a[1]++;
        res = (a[2]-a[0])/2 + (a[2]-a[1])/2;
        ++res;
        cout << res << endl;
        return 0;
    }

    //kgk
    if (a[0]%2!=0 && a[1]%2 == 0 && a[2]%2 !=0) {
        a[2]++;
        a[0]++;
        res = (a[2]-a[0])/2 + (a[2]-a[1])/2;
        ++res;
        cout << res << endl;
        return 0;
    }
    //kkk
    if (a[0]%2!=0 && a[1]%2 != 0 && a[2]%2 !=0) {
        res = (a[2]-a[0])/2 + (a[2]-a[1])/2;
        cout << res << endl;
        return 0;
    }
    cout << res << endl;
    return 0;
}