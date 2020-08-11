# 공백을 기준으로 입력받음
N, M, K = map(int, input().split())
# N 개의 숫자를 공백으로 구분하여 입력받음
data = list(map(int, input().split()))
data.sort(reverse=True) # 역순으로 정렬된 상황
first = data[0]
second = data[1]

count = M // (K + 1) * K
count += M % (K + 1)

ans = count * first
ans += (M // (K + 1)) * data[1]

print(ans)

