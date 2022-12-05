# 내 풀이
n = int(input())
x = 1
y = 1
arr = list(input().split())
for i in range(len(arr)):
    if arr[i] == "R":
        y+= 1
    elif arr[i] == "U":
        x -= 1
        if x == 0:
            x += 1
    elif arr[i] == "L":
        y -= 1
        if y == 0:
            y += 1
    else:
        x += 1

print(x,y)

# 책 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x,y)
            