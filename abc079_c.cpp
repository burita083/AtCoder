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
    string s, t;
    int N;
    cin >> s;
    N = s.size();
    t = s[0];
    int sum = 0;
    rep(i, 0, 1<<(N-1)) {
        int a;
        sum = s[0] - '0';
        t = s[0];
        rep(j, 0, N - 1) {
            a = s[j+1] - '0';
            if(i & (1<<j)) {
                sum += a;
                t = t + '+' + s[j+1];
            } else {
                sum -= a;
                t = t + '-' + s[j+1];
            }
        }

        if(sum == 7) {
            cout << t << "=7" << endl;
            break;
        }
    }
    return 0;
}