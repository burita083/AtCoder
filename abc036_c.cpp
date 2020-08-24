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
    int n; 
    cin >> n;
    vector<int> a(n);
    rep(i, 0, n) {
        cin >> a[i];
    }
    vector<int> t = a;
    sort(ALL(t));
    t.erase(unique(ALL(t), end(t)));
    map<int, int> m;
    for (int i = 0; i < (int) t.size(); ++i) {
        m[t[i]] = i;
    }    

    for (auto& e : a) {
        cout << m[e] << endl;
    }
    return 0;
}