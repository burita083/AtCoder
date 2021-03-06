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
using namespace std;
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
map<int, int> ans;
void f(int n) {
    for (int i = 2; i * i <= n; i++) {
        if (n % i != 0) continue;
        while (n % i == 0) {
            n /= i;
            ans[i]++;
        }
    }
    if (n != 1) ans[n]++;
}

// 約数列挙 O(√n)
vector<ll> divisor(ll n){
    vector<ll> res;
    for(ll i = 1; i * i <= n; i++){
        if(n % i == 0){
            res.push_back(i);
            if(i != n / i) res.push_back(n / i);
        }
    }
    return res;
}

map<int, int> prime_factor(int n) {
    map<int, int> res;
    for (int i = 2; i * i <= n; i++) {
        while (n % 1 == 0) {
            ++res[i];
            n /= i;
        }
    }
    if (n != 1) res[n] = 1;
    return res;
}

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) f(i);
 
    long long A = 1;
    for (int i = 1; i <= n; i++) {
        if (ans.count(i)) {
            (A *= (ans[i] + 1)) %= MOD;
        }
    }
 
    cout << A << endl;
    return 0;
}