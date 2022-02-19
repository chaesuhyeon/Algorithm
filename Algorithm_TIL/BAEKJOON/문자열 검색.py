# 3085 사탕 게임
def count(arr):
    n = len(arr)
    answer = 1

    for i in range(n):
        # 열 순회하면서 연속되는 숫자 세기
        cnt =1
        for j in range(1,n):
            if arr[i][j] == arr[i][j-1]: # 이전 것과 문자가 같다면 cnt + 1
                cnt += 1
            else: # 이전 것과 다르다면
                cnt = 1 # 다시 1로 초기화

            if cnt > answer: # 비교해서 cnt가 더 크다면 answer갱신
                answer = cnt

        # 행 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1,n):
            if arr[j][i] == arr[j-1][i]:
                # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else: # 이전 것과 다르다면 다시 1로 초기화
                cnt = 1

            if cnt > answer:
                answer = cnt
    return(answer)


n = int(input())
arr=[list(input()) for _ in range(n)]
answer=0

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j+1 < n:
        	# 인접한 것과 바꾸기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            
            # count는 arr에서 인접한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp=count(arr)

            if temp > answer:
                answer = temp
               
            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        # 행 바꾸기
        if i+1 < n:
        	# 인접한 것과 바꾸기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
            # count는 arr에서 인접한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp=count(arr)

            if temp > answer:
                answer = temp
            
            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
print(answer)


# 1018 체스판 다시 칠하기

N , M = map(int, input().split())
chess = [input() for _ in range(N)]
cnt = []

for n in range(N-7): # 시작점
    for m in range(M-7): # 시작점
        W = 0 # W로 시작할 경우 바꿔야할 체스판의 개수
        B = 0 # B로 시작할 경우 바꿔야할 체스판의 개수
        for i in range(n, n+8): # 8x8 만들어줌 , 시작점으로부터 8칸씩 체크
            for j in range(m, m+8): # 8x8 만들어줌 , 시작점으로부터 8칸씩 체크
                # 8*8로 자른 체스판이 W로 시작할 경우에 
                if (i+j) % 2 == 0:  #(i+j) % 2 == 0일 경우 W이어야 함 만약 W가 아니라면 W를 1증가시킴
                    # 마찬가지로 8*8로 자른 체스판이 'B'로 시작할 경우 바꿔야 할 체스판의 개수는 B에 저장
                    if chess[i][j] != 'W':
                        W += 1
                    if chess[i][j] != 'B':
                        B += 1
                else:  # (i+j) % 2 != 0 일 경우 'B'이어야 한다. 만약 'B'가 아니라면 W를 1증가시킨다.
                    # 마찬가지로 8*8로 자른 체스판이 'B'로 시작할 경우 바꿔야 할 체스판의 개수는 B에 저장
                    if chess[i][j] != 'B':
                        W += 1
                    if chess[i][j] != 'W':
                        B += 1
        cnt.append(min(W,B))
print(min(cnt))