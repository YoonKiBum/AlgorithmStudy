tc = int(input())
for i in range(tc):
    a = input()
    ans = 0
    for i in range(len(a)):
        if a[i] == "(":
            ans += 1
        elif a[i] == ")":
            ans -= 1
        if ans < 0:
            break
    if ans == 0:
        print("YES")
    else:
        print("NO")
