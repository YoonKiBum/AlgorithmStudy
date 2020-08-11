# 각 정보들 입력 받음
N, M, K = map(int, input().split())

# 수열 입력받음
data = list(map(int, input().split()))
data.sort(reverse=True)
first = data[0]
second = data[1]
total = 0

while True:
    for i in range(K):
        total += first
        M -= 1
        if M == 0:
            break
    total += second
    M -= 1
    if M == 0:
        break

print(total)

