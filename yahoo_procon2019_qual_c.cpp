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
#define showVector(v) rep(i,0,v.size()){p(v[i]);p(" ")} pl("")
#define p(s) std::cout << s ;
#define pl(s)  std::cout << s << endl;
using namespace std;
 
int main() {
    ll k, A, B;
    ll turn = 0; 
    ll b = 1;
    ll yen = 0;
    cin >> k >> A >> B;

    turn += A-1;
    b = A;
    ll temp = b;

    b = 0;
    yen++;
    turn++;
    temp++;

    b = B;
    yen--;
    turn++;
    temp++;

    if (temp > b) {
        cout << (1+k) << endl;
    } else {
        ll K = k - turn;
        ll current = b;
        while(turn <= K) {
            if (K-turn > 2) {
                current -= A;
                current += B;
                turn += 2;
            } else {
                current++;
                turn++;
            }
        }
        cout << turn << endl;
        cout << current << endl;
    }
    return 0;
}