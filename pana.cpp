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

struct Node {
    int y;
    int x;
};
queue<Node> que;
int R, C;
int sy, sx, gy, gx;
int y, x, depth;

int bfs() {
    vector<vector<int> >  vec(1000000000, vector<int>(1000000000));
    int y_vec[] = {-1 ,1, -1, 1};
    int x_vec[] = {-1, 1, 1, -1};
    int count = 0;
    while (!que.empty()) {
        Node node = que.front(); que.pop();
        y = node.y;
        x = node.x;

        for (int i = 0; i < 4; ++i) {
            Node next = {y + y_vec[i], x + x_vec[i]};

            if (0 <= next.y && next.y <= R-1 && 0 <= next.x && next.x <= C - 1 && vec[next.y][next.x] != 'x') {
                vec[next.y][next.x] = 'x';
                que.push(next);
            }
            ++count;
        }
    }
    return 0;
}
 
int main() {
    cin >> R >> C;
    Node start = {0, 0};
    que.push(start);
    cout << bfs() << endl;
    return 0;
}
