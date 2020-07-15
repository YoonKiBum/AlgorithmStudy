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
	check[x][y] = true; // Ž���� �Ѱ��� ǥ������

	for (int j = 0; j < 3; j++) // �̵��� 3���� �������� ������ �ǹǷ�
	{
		int nX = x + mx[j]; // ���� �̵��� ���� ��ǥ
		int nY = y + 1; // ���� �̵��� ���� ��ǥ

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
	// ������� ������ �ϱ� ���� �ڵ�
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> R >> C;
	
	for (int i = 0; i < R; i++) // input���� �Է¹���
	{
		for (int j = 0; j < C; j++)
		{
			cin >> arr[i][j];
		}
	}

	int total = 0;

	for (int i = 0; i < R; i++) // ���� ���� ��ŭ �Լ��� ȣ��
	{
		total += maxNumOfPipes(i, 0);
	}

	cout << total << endl;
	return 0;
}


