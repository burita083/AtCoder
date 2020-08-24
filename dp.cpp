#include <vector>
#include <math.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <deque>

typedef long long ll;
#define rep(i, n) for(int i = 0; i<n; i++)
#define ALL(a) begin(a), end(a)
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
vector<int> vec;

// fibをdpで解く例
int dp[100];
int fib(int n) {
    if (dp[n] != -1) return dp[n];
    dp[n] = fib(n - 1) + fib(n - 2);
    return dp[n];
}

// DP テーブル
long long dp[100010];

// DP テーブル全体を初期化 (最小化問題なので INF に初期化)
for (int i = 0; i < 100010; ++i) dp[i] = INF;

// 初期条件
dp[0] = 0;

// ループ
for (int i = 0; i < N; ++i) {
    chmin(dp[なにか], dp[なにか] + なにか);
    ...
}

int main() {
    string s;
    int i;
    rep(i, 100) {
        dp[i] = -1;
    }
    dp[0] = 0;
    dp[1] = 1;
    cout << fib(10) << endl;
    return 0;
}