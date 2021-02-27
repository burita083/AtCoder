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
int R, C;
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

            if (0 <= next.y && next.y <= R-1 && 0 <= next.x && next.x <= C - 1 && vec[next.y][next.x] == '.') {
                vec[next.y][next.x] = 'x';
                que.push(next);
            }
        }
    }
    return 0;
}
 
int main() {
    int count = 0;
    cin >> R >> C;
    cin >> sy >> sx >> gy >> gx;
    --sy;
    --sx;
    --gy;
    --gx;
    vec.resize(R);
    for (int i = 0; i < R; ++i) {
        cin >> vec[i];
    }

    Node start = {sy, sx, 0};
    que.push(start);
    int dep = bfs();
    cout << dep << endl;
    return 0;
}
