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
vector<int> vec;
int main() {
    string day;
    cin >> day;
    map<string, int> days;
    days["Sunday"] = 0;
    days["Monday"] = 5;
    days["Tuesday"] = 4;
    days["Wednesday"] = 3;
    days["Thursday"] = 2;
    days["Friday"] = 1;
    days["Saturday"] = 0;
    //vector<vector<int>> data(3, vector<int>(4));

    //初期値0
    //vector<int> data(i, 0);
    cout << days[day] << endl;
    return 0;
}