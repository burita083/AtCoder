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
    vector<vector<char> > vec(4, vector<char>(4));
    vector<vector<char> > vec2(4, vector<char>(4));
    rep(i, 0, 4) {
        rep(j, 0, 4) {
            cin >>vec[i][j];
            vec2[i][j] = vec[i][j];
        }
    }

    vec[0][0] = vec2[3][3];
    vec[0][1] = vec2[3][2];
    vec[0][2] = vec2[3][1];
    vec[0][3] = vec2[3][0];
    vec[1][0] = vec2[2][3];
    vec[1][1] = vec2[2][2];
    vec[1][2] = vec2[2][1];
    vec[1][3] = vec2[2][0];
    vec[2][0] = vec2[1][3];
    vec[2][1] = vec2[1][2];
    vec[2][2] = vec2[1][1];
    vec[2][3] = vec2[1][0];
    vec[3][0] = vec2[0][3];
    vec[3][1] = vec2[0][2];
    vec[3][2] = vec2[0][1];
    vec[3][3] = vec2[0][0];

    rep(i, 0, 4) {
        rep(j, 0, 4) {
            cout << vec[i][j];
            cout << " ";
        }
        cout << endl;
    }
    return 0;
}