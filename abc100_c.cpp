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
int main() {
    int N;
    cin >> N;
    vl a(N);
    rep(i, 0, N) {
        cin >> a[i];
    }
    int count = 0;
        rep(i, 0, a.size()) {
            while(true) {
                if (a[i] % 2 == 0) {
                    a[i] = a[i] / 2;
                    ++count;
                } else {
                    break;
                }
            }
        }
    cout << count << endl;
    return 0;
}