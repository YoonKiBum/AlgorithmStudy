# Àç±Í ¹æ½ÄÀ¸·Î ÀÌÁø Å½»ö ±¸Çö
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


N = int(input())
data = list(map(int, input().split()))

M = int(input())
order = list(map(int, input().split()))

for i in range(M):
    result = binary_search(data, order[i], 0, N - 1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
