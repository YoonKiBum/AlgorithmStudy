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

	for (int i = n - 1; i >= 0; i--) // 동전을 큰 가치부터 나누기 위해 역순으로 배열을 조회함
	{
		if (amount / a[i] == 0) // 입력받은 금액보다 가치가 큰 경우 동전의 갯수를 카운트 하지 않고 넘김
		{
			amount %= a[i];
		}
		// 입력받은 금액보다 가치가 작은 경우 그 몫 만큼 동전을 카운트 함
		// ex) 입력받은 금액 4200원 가치 1000원일 경우 나눈 몫인 동전4개를 카운트 한 후 나머지인
		 // 200원을 넘겨줌
		else if (amount / a[i] != 0)  
		{
			count += (amount) / a[i];
			amount %= a[i];
		}
	}

	cout << count; // 동전의 갯수를 출력해줌

	return 0;
}

