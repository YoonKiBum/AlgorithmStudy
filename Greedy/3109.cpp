#include <iostream>
#define MAX 10001
#define MAX2 501

using namespace std;
char arr[MAX][MAX2];
bool check[MAX][MAX2] = { false };
int R, C;
int mx[3] = { -1,0,1 };

int maxNumOfPipes(int x, int y)
{
	if (y == C - 1)
	{
		return 1;
	}
	check[x][y] = true; // 탐색을 한것을 표시해줌

	for (int j = 0; j < 3; j++) // 이동은 3가지 방향으로 제한이 되므로
	{
		int nX = x + mx[j]; // 다음 이동할 행의 좌표
		int nY = y + 1; // 다음 이동할 열의 좌표

		if (nX >= 0 && nY >= 0 && check[nX][nY] == false && arr[nX][nY] != 'x' && nX <= R - 1 && nY <= C - 1)
		{
			int val = maxNumOfPipes(nX, nY);
			if (val)
			{
				return val;
			}
		}
	}
	return 0;
}

int main(void)
{
	// 입출력을 빠르게 하기 위한 코드
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> R >> C;
	
	for (int i = 0; i < R; i++) // input값을 입력받음
	{
		for (int j = 0; j < C; j++)
		{
			cin >> arr[i][j];
		}
	}

	int total = 0;

	for (int i = 0; i < R; i++) // 행의 개수 만큼 함수를 호출
	{
		total += maxNumOfPipes(i, 0);
	}

	cout << total << endl;
	return 0;
}


