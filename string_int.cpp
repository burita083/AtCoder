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
int main() {
    // +=でインクリメントしていく場合は初期値を0にする
    int N, A, B, ans = 0;
    //vector<vector<int>> data(3, vector<int>(4));
    cin >> N >> A >> B;
    rep(i, 1, N+1) {
        // intをstringに変換
        string s = to_string(i);
        int len = 0;
        // 長さはlength()
        rep(i, 0, s.length()) {
            // -48を引けば、charからintの値を求めることが可能
            len += s[i] - 48;
        }
        if (len >= A && len <= B) {
            ans += i;
        }
    }
    cout << ans << endl;
    return 0;
}