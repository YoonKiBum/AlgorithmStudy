#include <iostream>
#define MAX 10001 
#define MAX2 501
using namespace std;

char arr[MAX][MAX2];
bool check[MAX][MAX2] = { false };

void maxOfPipe(int row, int col)
{
	int count = 0;
	int i = 0, j = 0;
	for (i = 0; i < row; i++)
	{
		for (j = 0; j < col; j++)
		{
			int k = i, l = j;
			if (j == col - 1)
			{
				count++;
				break;
			}

			if (i == 0) // 첫 행인 경우
			{
				if (arr[k][++l]!='x' && check[k][l] == false)
				{
					check[k][l] = true;
					continue;
				}
				else if (arr[++k][l] != 'x' && check[k][l] == false)
				{
					check[k][l] = true;
					i = k;
					continue;
				}
				else
				{
					break;
				}
			}
			else if (i >= 1 && i < row - 1) // 두번째 행부터 마지막 행 사이인 경우
			{
				if (arr[--k][++l] != 'x' && check[k][l] == false)
				{
					check[k][l] = true;
					i = k;
					continue;
				}
				else if (arr[++k][l] != 'x' && check[k][l] == false)
				{
					check[k][l] = true;
					i = k;
					continue;
				}
				else if (arr[++k][l] != 'x' && check[k][l] == false)
				{
					check[k][l] = true;
					i = k;
					continue;
				}
				else
				{
					break;
				}
			}
			else // 마지막 행인 경우
			{
				if (arr[--k][++l] != 'x' && check[k][l] == false)
				{
					check[k][l] = true;
					i = k;
					continue;
				}
				else if (arr[++k][l] != 'x' && check[k][l] == false)
				{
					check[k][l] = true;
					i = k;
					continue;
				}
				else
				{
					break;
				}
			}
		}
	}
	cout << count << endl;
}

int main(void)
{
	// 입출력을 빠르게 학기 위한 코드
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int R, C;
	cin >> R >> C;

	for (int i = 0; i < R; i++) // input값 입력을 받음
	{
		for (int j = 0; j < C; j++)
		{
			cin >> arr[i][j];
		}
	}

	maxOfPipe(R, C);
	return 0;
}

