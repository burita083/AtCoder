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
vector<string> vec;
vector<vector<bool> > reached;
void search(int x, int y);
int H, W, count, res;
int s_y, s_x, g_y, g_x;

void search(int y, int x) {
    if (y < 0 || H <= y || x < 0 || W <= x)
		return;

    if (y == H && x == W) {
        res = min(count, res)
        return;
    }

    if (vec[y][x] == '#') {
         ++count;
    }

	if (reached[y][x]) {
		return;
    }

    reached[y][x] = true;
    search(y + 1, x);
	search(y, x + 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> H >> W;
    count = 0;
    res = INF;
    vec.resize(H);
    for (int i = 0; i < H; ++i) {
        cin >> vec[i];
    }

   	reached.resize(H, vector<bool>(W));

    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (vec[i][j] == 's') {
             s_y = i;
             s_x = j;
            }

            if (vec[i][j] == 'g') {
             g_y = i;
             g_x = j;
            }
        }
    }

    search(s_y, s_x);
    reached[g_y][g_x] ? cout << "Yes" : cout << "No";
    cout << endl;
    return 0;
}
