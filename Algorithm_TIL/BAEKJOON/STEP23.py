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

