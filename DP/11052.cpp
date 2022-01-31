#define MAX 1001
#include <bits/stdc++.h>

using namespace std;

int main(void) {
	int n, dp[MAX], data[MAX];
	scanf("%d", &n);


	for (int i = 0; i < n; i++) {
		scanf("%d", &data[i]);
	}
	dp[0] = data[0];

	for (int i = 1; i < n; i++) {
		dp[i] = max(data[i], dp[i - 1] + dp[0]);
		for (int j = 0; j < i / 2 + 1; j++) {
			dp[i] = max(dp[i], dp[j] + dp[i - j - 1]);
		}
 	}

	printf("%d", dp[n - 1]);
	return 0;
}
