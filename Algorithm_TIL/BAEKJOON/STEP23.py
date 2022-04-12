# 1260 DFS와 BFS
import sys
from collections import deque
n, m, start = map(int, sys.stdin.readline().split())
arr= [[] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n+1)
for i in range(m):
    group, node = map(int, sys.stdin.readline().split())
    arr[group].append(node)
    arr[node].append(group)

for i in range(1, n+1):
    arr[i].sort()

def dfs(start):
    print(start , end = ' ')
    visited[start] = 1

    for i in arr[start]:
        if visited[i] == 0:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        for i in arr[q]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

            
dfs(start)
print()
visited = [0] * (n+1)
bfs(start)


# 1012 유기농 배추
# dfs로 풀이 
import sys
sys.setrecursionlimit(10**6) # 재귀 함수 깊이 에러 방지하기 위해 사용
t = int(sys.stdin.readline())

def dfs(x,y):
    if x < 0 or x >= n or y<0 or y>=m :
        return False
    if arr[y][x] == 1:
        arr[y][x] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False



for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().split())
    arr =  [[0]*n for _ in range(m)]
    result = 0 
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        arr[b][a] = 1


    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1

    print(result)

# 2606 바이러스
import sys
computer = int(sys.stdin.readline())
n = int(sys.stdin.readline())

graph=[[]*(computer+1) for _ in range(computer+1)]
visited = [0] * (computer + 1)

result = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b) # 연관된 노드들 리스트에 넣어 줌 
    graph[b].append(a)

# graph :  [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

def dfs(num):
    global result
    visited[num] = 1

    for i in graph[num]:
        if visited[i] == 0:
            result += 1 # 처음 방문 하면 컴퓨터 개수 1개 추가 
            dfs(i) # i를 넘겨서 재귀로 호출. i를 방문 처리 해줌 

    return result

print(dfs(1)) # 1부터 시작


# 7576 토마토
# 최소라는 말이 있어서 bfs로 풀 생각함 - 이코테 미로찾기랑 비슷한듯

import sys
from collections import deque
m,n = map(int, sys.stdin.readline().split())

arr=[]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
queue = deque([])

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m):
        if arr[i][j] == 1: # 토마토 위치 넣어주기
            queue.append([i, j])


def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]            
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0: # 범위 안벗어나는지 확인 & 0일경우
                arr[nx][ny] = arr[x][y] + 1 # 누적 합 구해줌
                queue.append([nx, ny])

bfs() # 함수 실행해서 누적합들 다 구해줌
for i in arr: # arr에서 한행씩 뽑아서 (i)
    for j in i: # i에서 낱개로 뽑았을 때
        if j == 0: # 0이 하나라도 나오면 다 익히지 못했으므로 -1을 출력
            print(-1)
            exit(0) # 바로 종료 시킴 
    cnt = max(cnt, max(i)) # 정확한 마지막 위치를 모르기 때문에 한행 씩 뽑아서 최댓값이 있으면 그것으로 바꿔주기

print(cnt -1) # 1은 포함시키면 안되기 때문에 1빼줌(1부터 시작했기 때문에)   


# 2178 미로 탐색
import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())

result = []

for i in range(n):
    result.append(list(map(int, sys.stdin.readline().rstrip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if result[nx][ny] == 0:
                continue

            if result[nx][ny] == 1:
                result[nx][ny] = result[x][y]+1
                queue.append((nx,ny))

    return result[n-1][m-1]

print(bfs(0,0)) 

