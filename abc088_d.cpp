#include <vector>
#include <math.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <deque>
#include <map>
using namespace std;
struct Node {
    int y;
    int x;
    int depth;
};
queue<Node> que;
int H, W;
int sy, sx, gy, gx;
int y, x, depth;
vector<int> y_vec = {0, 0, -1, 1};
vector<int> x_vec = {-1, 1, 0, 0};
vector<string> vec;

int bfs() {
    while (!que.empty()) {
        Node node = que.front(); que.pop();
        y = node.y;
        x = node.x;
        depth = node.depth;
        if (y == gy && x == gx) return depth;

        for (int i = 0; i < 4; ++i) {
            Node next = {y + y_vec[i], x + x_vec[i], depth + 1};

            if (0 <= next.y && next.y <= H-1 && 0 <= next.x && next.x <= W - 1 && vec[next.y][next.x] == '.') {
                vec[next.y][next.x] = 'x';
                que.push(next);
            }
        }
    }
    return 0;
}
 
int main() {
    int count = 0;
    cin >> H >> W;
    sy = 0;
    sx = 0;
    gy = H - 1;
    gx = W - 1;
    vec.resize(H);
    for (int i = 0; i < H; ++i) {
        cin >> vec[i];
    }

    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (vec[i][j] == '.') ++count;
        }
    }

    Node start = {sy, sx, 1};
    que.push(start);
    int dep = bfs();
    if (dep != 0) {
        cout << (count - dep) << endl;
    } else {
        cout << -1 << endl;
    }
    return 0;
}
