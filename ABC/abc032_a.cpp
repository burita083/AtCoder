#include <vector>
#include <math.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <deque>

typedef long long ll;
#define rep(i, a, n) for(int i = a; i<n; i++)
#define ALL(a) begin(a), end(a)
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
vector<int> vec;
ll gcd(ll a, ll b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

// least common multiple 最小公倍数
ll lcm(ll a, ll b) {
    ll g = gcd(a, b);
    return a / g * b;
}

int main() {
    ll a, b, n;
    cin >> a >> b >> n;
    //vector<vector<int>> data(3, vector<int>(4));
    rep(i, n, 200001) {
        if (i >= n) {
            if (i % a == 0 && i % b == 0) {
                cout << i << endl;
                return 0;
            }
        }
    }
    return 0;
}