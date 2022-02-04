#include <bits/stdc++.h>
#define MAX 100001

using namespace std;

int graph[MAX];
int moves[] = { -1, 1, 2 };

void bfs(int n, int k) {
	int count = 0;
	queue<int> q;
	q.push(n);
	graph[n] = 1;
	if (n == k) {
		printf("%d", count);
		return;
	}

	while (!q.empty()) {
		int len = q.size();
		for (int i = 0; i < len; i++) {
			int x = q.front();
			q.pop();
			for (int i = 0; i < 3; i++) {
				int nx;
				if (i == 2)
					nx = x * moves[2];
				else
					nx = x + moves[i];
				if (nx < 0 || nx >= MAX)
					continue;
				if (graph[nx] == 0) {
					q.push(nx);
					graph[nx] = 1;
				}
				if (nx == k) {
					printf("%d", count+1);
					return;
				}
			}
		}
		count += 1;
	}
}

int main(void) {
	int n, k;
	scanf("%d %d", &n, &k);

	bfs(n, k);
	return 0;
}
