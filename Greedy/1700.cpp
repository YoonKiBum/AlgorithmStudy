#include <iostream>
#define MAX 101
using namespace std;

int main(void)
{
	// 입출력을 빠르게 하기 위한 코드 
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, K; // 구멍의 개수 , 총 사용횟수 
	int seq[MAX] = { 0 }; // 사용 순서 
	int cnt = 0;  // 플러그에 꽂혀 있는 개수
	int cnt2 = 0; // 플러그를 빼는 횟수
	int plug[MAX] = { 0 }; // 플러그에 꽃혀있는 정보를 담을 배열
	bool flag = false; // 다음에 꽂아야 할 코드가 지금 꽂혀있는지 알아보기 위한 bool형 변수 flag;

	cin >> N >> K;
	for (int i = 0; i < K; i++)
	{
		cin >> seq[i];
	}

	for (int i = 0; i < K; i++)
	{
		flag = false;
		for (int j = 0; j < N; j++) // 꽂아야할 기계가 이미 꽂혀있는 기계인지 판단
		{
			if (plug[j] == seq[i])
			{
				flag = true;
				break;
			}
		}
		if (flag == true) // 이미 꽂혀있는 코드면 넘어감
		{
			continue;
		}
		else // 이미 꽂혀있는 코드가 아닌 경우
		{
			if (cnt < N) //비어 있는 코드가 존재하면 코드를 꽂음
			{
				plug[cnt] = seq[i];
				cnt++;
			}
			else // 비어 있는 코드가 없고 이미 꽂혀있는 코드가 아닌경우 가장 나중에 사용되거나 앞으로 사용이 되지 않을 기계를 찾음
			{
				int idx = 0;
				int device = -1;
				
				for (int j = 0; j < N; j++)
				{
					int last = 0;
					
					for (int l = i + 1; l < K; l++)
					{
						if (plug[j] == seq[l])
						{
							break;
						}
						last++;
					}
					if (last > device)
					{
						idx = j;
						device = last;
					}
				}
				cnt2++;
				plug[idx] = seq[i];
			}
		}
	}
	cout << cnt2;
	return 0;
}

