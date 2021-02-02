n = int(input())
data = []
for i in range(n):
    data.append(input())

count = 0
for word in data:
    word += "!"
    alpha = [0] * 26
    check = True
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if alpha[ord(word[i]) - 97] == 0:
                alpha[ord(word[i]) - 97] = 1
            else:
                check = False
                break
    if check:
        count += 1

print(count)

