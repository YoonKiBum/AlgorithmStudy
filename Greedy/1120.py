x, y = map(str, input().split())
n = len(y) - len(x) + 1

min = int(1e9)

for i in range(n):
    count = 0
    for j in range(len(x)):
        if (x[j] != y[i+j]):
            count += 1
    if count < min:
        min = count
print(min)
