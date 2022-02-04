#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#define MAX 1001

using namespace std;
vector<int> graph[MAX];
bool visited[MAX];

void bfs(int start) {
	queue<int> q;
	q.push(start);
	visited[start] = true;

	while (!q.empty()) {
		int x = q.front();
		q.pop();
		for (int i = 0; i < graph[x].size(); i++) {
			int y = graph[x][i];
			if (!visited[y]) {
				visited[y] = true;
				q.push(y);
			}
		}
	}
}

int main(void) {
	int n, m;
	int count = 0;
	scanf("%d %d", &n, &m);

	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	for (int i = 1; i < n+1; i++) {
		sort(graph[i].begin(), graph[i].end());
	}

	for (int i = 1; i < n + 1; i++) {
		if (!visited[i]) {
			bfs(i);
			count += 1;
		}
	}

	printf("%d", count);
	return 0;
}
