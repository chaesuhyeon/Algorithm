n, m = map(int, input().split())
arr =[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

s = 0
for i in arr:
    if min(i) > s: # 카드는 무조건 1이상의 값부터 시작하기 때문에 s에 새로운 min의 값이 무조건 대입이 되며, 기존의 s보다 클 경우 s에 한 행의 최솟값을 대입해줌
        s = min(i)
    else:
        continue # s보다 한 행의 최솟값이 작을 경우 무시

print(s) # 최솟값 출력 