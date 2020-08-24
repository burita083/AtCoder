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
    int N;
    cin >> N;
    vi a(N);
    rep(i, 0, N) {
        cin >> a[i];
    }
    int answer = 0;
    while (*max_element(a.begin(), a.end()) > 0) {
        int i = 0;
        while (i < N) {
            if (a[i]  == 0) {
                ++i;
            } else {
                while(i < N && a[i] > 0) {
                    --a[i];
                    ++i;
                }
                ++answer;
            }
        }
    }

    cout << answer << endl;
    return 0;
}