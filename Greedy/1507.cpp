#include <iostream>
#define MAX 20

using namespace std;

int arr[MAX][MAX] = { 0 }; // 도시와 도시 사이의 시간을 담을 배열
int arr2[MAX][MAX] = { 0 }; // 복사본
void floydWarshall(int n)
{
	int total = 0;
	
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			arr2[i][j] = arr[i][j];
		}
	}

	for (int k = 0; k < n; k++)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (i == j || j == k || i == k)
				{
					continue;
				}
				else if (arr[i][k] + arr[k][j] < arr[i][j])
				{
					cout << -1;
					return;
				}
				else if (arr[i][k] + arr[k][j] == arr[i][j])
				{
					arr2[i][j] = 0;
				}
			}
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			total += arr2[i][j];
		}
	}

	cout << total/2 << endl;
}

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N; // 도시의 개수 
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> arr[i][j];
		}
	}

	floydWarshall(N);

	return 0;
}
