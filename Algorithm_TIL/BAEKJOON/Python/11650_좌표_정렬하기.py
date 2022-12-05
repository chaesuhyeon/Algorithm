n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append((a,b)) # [(1, 1), (1, -1), (2, 2), (3, 4), (3, 3)]

arr.sort(key= lambda x:(x[0], x[1])) # 첫 번째 숫자를 기준으로 정렬 후 두번 째 숫자도 순서대로 정렬

for i in arr:
    print(*i)