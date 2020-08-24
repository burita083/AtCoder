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
    int count = 0;
    cin >> N;
    rep(i, 1, N+1) {
        int ans = 1;
        vi a(N + 1);
        int num = i;
        rep(i, 2, N+1) {
            while (num % i == 0) {
                a[i]++;
                num /= i;
            }
        }

        rep(i, 2, N+1) {
            ans *= a[i] + 1;
        }
        if (ans == 8 && i % 2 != 0) {
            ++count;
        } 
    }
    cout << count << endl;
    return 0;
}