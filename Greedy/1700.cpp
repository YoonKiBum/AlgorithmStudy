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
			else // 비어 있는 코드가 없고 이미 꽂혀있는 코드가 아닌경우
			{
				int idx = 0;
				int device = -1;
				
				for (int j = 0; j < N; j++)
				{
					int last = 0;
					for (int l = i + 1; l < K; l++) // 꽂아야 할 기계의 다음부터 끝까지 조회하며 가장 최소로 뽑을 수 있는 기계를 찾아서 뽑음
					{
						if (plug[j] == seq[l]) // 조회한게 꽂혀 있는 경우
						{
							break;
						}
						last++; // 조회한게 꽂혀 잊지 않은 경우 하나 증가시킴
					}
					if (last > device) // last가 device보다 크다면 
					{
						idx = j; // idx를 j로 재정의
						device = last; // device에 last를 넣음
					}
				}
				cnt2++; // cnt2를 하나 증가시킴
				plug[idx] = seq[i]; // 뽑아야 할 위치에 새로 추가함
			}
		}
	}
	cout << cnt2; // cnt2 출력
	return 0;
}

