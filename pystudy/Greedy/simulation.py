# N, M; °£´ÜϰÔ°ø ±â8·ÎÀ·Â¹Þ½
N, M = map(int, input().split())

# ½ÃÛ¡, ¹æ À·¹Þ½
xPos, yPos, Direction = map(int, input().split())

# ¹湮 ¿©ºθ¦ ǥÇÇ ÀÂ¿øºƮ d »ý= [[0] * M for _ in range(N)]
d[xPos][yPos] = 1  # ½ÃÛ¡ 'ġ¸¦ ¹湮Ç °Í¸·Îǥ½Ã
# ¸Êdº¸¸¦ ÆÇÇ ÀÂ¿øºƮ À·Â¹Þ½
array = []
for i in range(N):
    array.append(list(map(int, input().split())))


# ¿ÞÊ¸·ÎȸÀ Ç´ÂÇ¼ö¼º ºÏÊÎ°æ ¿ÞÊ¸·ÎȸÀÇ ½Ã38·Î¹ٲÞdef turn_left():
    global Direction
    if Direction == 0:
        Direction = 3
    else:
        Direction -= 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 1
num_of_turn = 0

while True:
    turn_left()
    nx = xPos + dx[Direction]
    ny = yPos + dy[Direction]
    if array[nx][ny] == 0 and d[nx][ny] == 0:  # Ç´çöÌ¹湮 ¾ÈÑö̰í°ÁÀ °æ
        d[nx][ny] = 1
        xPos = nx
        yPos = ny
        count += 1
        num_of_turn = 0
        continue
    else:  # Ç´çöÌ¹湮µÈÁ¿ªÀ°ųª 0Á°¡ ¾ƴÑ°æ
        num_of_turn += 1
    if num_of_turn == 4:
        nx = xPos - dx[Direction]
        ny = yPos - dy[Direction]
        if array[nx][ny] == 0:
            xPos = nx
            yPos = ny
        else:  # Ç´çöÌ¹ٴÙÎ°æ
            break
        num_of_turn = 0

print(count)


