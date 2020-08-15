#include <iostream>
#include <algorithm> 
#define MAX 11

using namespace std;
int a[MAX];
int n, amount;

int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int count = 0;

	cin >> n >> amount;

	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}

	for (int i = n - 1; i >= 0; i--) // ������ ū ��ġ���� ������ ���� �������� �迭�� ��ȸ��
	{
		if (amount / a[i] == 0) // �Է¹��� �ݾ׺��� ��ġ�� ū ��� ������ ������ ī��Ʈ ���� �ʰ� �ѱ�
		{
			amount %= a[i];
		}
		// �Է¹��� �ݾ׺��� ��ġ�� ���� ��� �� �� ��ŭ ������ ī��Ʈ ��
		// ex) �Է¹��� �ݾ� 4200�� ��ġ 1000���� ��� ���� ���� ����4���� ī��Ʈ �� �� ��������
		 // 200���� �Ѱ���
		else if (amount / a[i] != 0)  
		{
			count += (amount) / a[i];
			amount %= a[i];
		}
	}

	cout << count; // ������ ������ �������

	return 0;
}

