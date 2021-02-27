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
int main() {
    string s;
    cin >> s;

    ll sum = 0;
    int n = s.size();

    for(int temp = 0; temp < (1 << n-1); ++temp) {
        ll t = s[0] - '0';

        for(int i = 0; i < n - 1; ++i) {
            if(temp & (1 << i)) {
                sum += t;
                t = s[i+1] - '0';
            } else {
                t *= 10;
                t += s[i+1] - '0';
            }
        }
        sum += t;
    }

    cout << sum << endl;
    return 0;
}