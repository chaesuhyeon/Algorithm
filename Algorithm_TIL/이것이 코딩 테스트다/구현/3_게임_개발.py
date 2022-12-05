n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1 

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
 
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
 
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break
        turn_time = 0

print(count)

# 먼저 n, m을 공백으로 구분하여 입력받고 방문한 위치를 저장하기 위한 맵(d)을 생성하여 0으로 초기화한다.
# 여기서 현재 캐릭터의 좌표 값을 1로 갱신하여 방문 처리한다.
# 반복문을 통해 전체 맵 정보를 입력받고 리스트 dx, dy를 통해 북, 동, 남, 서 방향을 정의한다.
# while문을 통해 시뮬레이션을 시작하는데, 먼저 turn_left( ) 메서드를 통해 캐릭터가 바라보는 방향을 왼쪽으로 회전한다.
# turn_left( ) 메서드에서는 방향 값을 1 감소시키는데 만약 그 값이 -1이라면 서쪽에 해당될 수 있도록 3으로 갱신해준다.
# 캐릭터가 바라보는 방향을 왼쪽으로 회전한 후에는 정면에 가보지 않은 칸이 존재하는 경우 이동할 수 있도록 하고,
# 정면에 가보지 않은 칸이 없거나 바다인 경우에는 변수 turn_time의 값을 1 증가시킨다.
# 만약 turn_time의 값이 4일 경우, 네 방향 모두 갈 수 없기 때문에 뒤로 이동할 수 있는지 확인하여 이동할 수 있다면
# 이동하고 그렇지 않다면 반복문을 종료한다.