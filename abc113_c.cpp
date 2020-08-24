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
    int N, M;
    cin >> N >> M;

    vector<vector<int> > ans(M, vector<int>(2, 0));
    vector<vector<pair<int, int> > > p(N, vector<pair<int, int> >());
    rep(i, 0, M) {
        int P, Y;
        cin >> P >> Y;
        P--;
        ans[i][0] = P;
        p[P].push_back(make_pair(Y, i));
    }

    rep(i, 0, N){
        sort(p[i].begin(), p[i].end());
        rep(j, 0, p[i].size()) {
            ans[p[i][j].second][1] = j + 1;
        }
    }

    rep(i, 0, M) {
        cout << setfill('0') << setw(6) << ans[i][0] + 1;
        cout << setfill('0') << setw(6) << ans[i][1] << endl;
    }
    return 0;
}