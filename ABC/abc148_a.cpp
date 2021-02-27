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
    int A, B;
    cin >> A >> B;
    if (A == 1 && B == 2) {
        cout << 3 << endl;
    }

    if (A == 1 && B == 3) {
        cout << 2 << endl;
    }
    if (A == 2 && B == 1) {
        cout << 3 << endl;
    }

    if (A == 2 && B == 3) {
        cout << 1 << endl;
    }

    if (A == 3 && B == 1) {
        cout << 2 << endl;
    }

    if (A == 3 && B == 2) {
        cout << 1 << endl;
    }
    return 0;
}