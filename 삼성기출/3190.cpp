#include <bits/stdc++.h>
#define MAX 101

using namespace std;
int n, k;
int graph[MAX][MAX];
int l;
queue<pair<int, char>> dir;
queue<pair<int, int>> snake;
int direction;
int dx[] = { -1, 1, 0, 0 };
int dy[] = { 0, 0, -1, 1 };

int moveDirection(int direction, char dInfo) {
	if (direction == 0) {
		if (dInfo == 'L')
			return 2;
		else
			return 3;
	}
	else if (direction == 1) {
		if (dInfo == 'L')
			return 3;
		else
			return 2;
	}
	else if (direction == 2) {
		if (dInfo == 'L')
			return 1;
		else
			return 0;
	}
	else {
		if (dInfo == 'L')
			return 0;
		else
			return 1;
	}
}

int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	cin >> k;
	for (int i = 0; i < k; i++) {
		int a, b;
		cin >> a >> b;
		graph[a - 1][b - 1] = 1;
	}

	cin >> l; 
	for (int i = 0; i < l; i++) {
		int a;
		char c;
		cin >> a >> c;
		dir.push(make_pair(a, c));
	}

	int time = 1;
	direction = 3;
	int xPos = 0, yPos = 0;
	graph[xPos][yPos] = 2;
	snake.push(make_pair(xPos, yPos));
	int tInfo = dir.front().first;
	char dInfo = dir.front().second;
	dir.pop();

	while (true) {
		xPos += dx[direction];
		yPos += dy[direction];
		if (xPos < 0 || yPos < 0 || xPos >= n || yPos >= n) {
			break;
		}
		if (graph[xPos][yPos] == 2) {
			break;
		}
		snake.push(make_pair(xPos, yPos));
		if (graph[xPos][yPos] != 1) { // 사과없는 경우
			int x = snake.front().first;
			int y = snake.front().second;
			graph[x][y] = 0;
			snake.pop();
		}
		if (graph[xPos][yPos] == 0) { // 사과 있는 경우
			graph[xPos][yPos] = 0;
		}
		graph[xPos][yPos] = 2;
		if (time == tInfo) {
			direction = moveDirection(direction, dInfo);
			if (!dir.empty()) {
				tInfo = dir.front().first;
				dInfo = dir.front().second;
				dir.pop();
			}
		}
		time++;
	}
	
	cout << time;
	return 0;
}
