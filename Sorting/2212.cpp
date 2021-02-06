#include <iostream>
#include <algorithm>
#include <vector>
#define MAX 10001

using namespace std;
vector<int> vec;
vector<int> dif;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, K;

	cin >> N;
	cin >> K;

	if (K >= N)
	{
		cout << 0;
		return 0;
	}

	else
	{
		int result = 0;

		for (int i = 0; i < N; i++)
		{
			int n;
			cin >> n;
			vec.push_back(n);
		}
		
		sort(vec.begin(), vec.end());

		for (int i = 0; i < N-1; i++)
		{
			dif.push_back(vec[i + 1] - vec[i]);
		}

		sort(dif.begin(), dif.end());

		for (int i = 0; i < N - K; i++)
		{
			result += dif[i];
		}
		cout << result;
	}
	return 0;
}
