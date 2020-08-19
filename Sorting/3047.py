data = list(map(int, input().split()))
word = list(input())
data.sort()

for i in word:
    print(data[(ord(i) - 65)], end=" ")
