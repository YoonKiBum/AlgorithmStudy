#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#define MAX 26

using namespace std;

int graph[MAX][MAX];
int dx[] = { -1, 1, 0, 0 };
int dy[] = { 0, 0, -1, 1 };
bool visited[MAX][MAX];
vector<int> vec;

void bfs(int xPos, int yPos, int n) {
	queue<pair<int, int>> q;
	q.push({ xPos, yPos });
	int count = 1;
	visited[xPos][yPos] = true;
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 || ny < 0 || nx >= n or ny >= n)
				continue;
			if (graph[nx][ny] != 0 && visited[nx][ny] == false) {
				q.push({ nx, ny });
				count += 1;
				visited[nx][ny] = true;
			}
		}
	}
	vec.push_back(count);
}

int main(void) {
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%1d", &graph[i][j]);
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (graph[i][j] != 0 && visited[i][j] == false) {
				bfs(i, j, n);
			}
		}
	}

	sort(vec.begin(), vec.end());

	printf("%d\n", vec.size());
	for (int i = 0; i < vec.size(); i++) {
		printf("%d\n", vec[i]);
	}
	return 0;
}
