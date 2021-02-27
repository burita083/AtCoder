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
vector<string> vec;
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
                que.push(next);
            }
        }
    }
    return 0;
}
 
int main() {
    cin >> H >> W;
    vec.resize(H);
    for (int i = 0; i < H; ++i) {
        cin >> vec[i];
    }

    vector<pair<int, int> > sg;
    for (int h = 0; h < H; ++h) {
        for (int w = 0; w < W; ++w) {
            if (vec[h][w] == '.') {
                pair<int, int> p = make_pair(h, w);
                sg.push_back(p);
            }
        }
    }
    int res = -1;
    for (int i = 0; i < sg.size(); ++i) {
        sy = sg[i].first;
        sx = sg[i].second;
        for (int j = 1; j < sg.size(); ++j) {
            gy = sg[j].first;
            gx = sg[j].second;
            Node start = {sy, sx, 0};
            queue<Node> empty;
            swap(que, empty);
            que.push(start);
            res = max(res, bfs());
        }
    }
    cout << res << endl;
    return 0;
}
