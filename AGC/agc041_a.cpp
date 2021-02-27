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
    ll N, A, B;
    cin >> N >> A >> B;
    ll answer = 0;
    if ((B - A) % 2 == 0) {
        ll a = (B + A) / 2;
        cout << a - A << endl;
        return 0;
    } else {
        if (N - B <= A - 1) { // Bのほうが近い
            while(true) {
                ++A;
                ++B;
                ++answer;
                if (B == N) {
                    ++A;
                    ++answer;
                    if (A == B) {
                        cout << answer << endl;
                        return 0;
                    }

                    if ((B - A) % 2 == 0) {
                        ll a = (B + A) / 2;
                        cout << (a - A) + answer << endl;
                        return 0;
                    } else {
                        ++A;
                        ++B;
                        ++answer;
                    }
                }
            }
        } else { // Aが近い
            while(true) {
                --A;
                --B;
                ++answer;
                if (A == 1) {
                    --B;
                    ++answer;
                    if (A == B) {
                        cout << answer << endl;
                        return 0;
                    }

                    if ((B - A) % 2 == 0) {
                        ll a = (B + A) / 2;
                        cout << (a - A) + answer << endl;
                        return 0;
                    } else {
                        --A;
                        --B;
                        ++answer;
                    }
                }
            }
        }
    }
    return 0;
}