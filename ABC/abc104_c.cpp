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
    string s;
    int D;
    ll G;
    cin >> D >> G;
    ll dp[1000];
    vector<pair<ll, ll> > data(D);
    //初期値0
    //vector<int> data(i, 0);
    vl a(D);
    rep(i, 0, D) {
        cin >> data[i].first;
        cin >> data[i].second;
    }
    int count = 1000000;
    ll ans = 0;
    bool found = false;
    ll mg = 10000000;
    ll sum = 0;
    while(found == false) {
        rep(i, 0, data.size()) {
            int temp = 0;
            ll g = G;
            rep(j, 0, data[i].first) {
                g -= 100 * (i + 1);
                if (j == data[i].first - 1) {
                    g -= data[i].second;
                }
                if (g <= 0) {
                    found = true;

                    temp = j + 1;
                    count = min(count, temp);
                }
            }

            if (!found) {
                mg = g;
            }
        }
        
        if (!found) {
            G = mg;
            sum += data.back().first;
            data.pop_back();
        } else {
            sum += count;
        }
    }
    cout << sum << endl;
    return 0;
}