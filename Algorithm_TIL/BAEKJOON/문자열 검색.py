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


# 1051 숫자 정사각형
N, M = map(int, input().split())
 
d = min(N, M) # 더 작은 값을 기준으로 함 / 둘 중 최소길이가 사각형 최대라서...?
 
array = []
for _ in range(N):
    array.append(list(map(int, input())))
 
answer = 1 # 어떤 직사각형이 입력되든 가장 작은 정사각형 값은 1이므로 1로 초기화
for i in range(N):
    for j in range(M):
        for k in range(1, d):
            if i + k < N and j + k < M: # 인덱스 범위 안넘는 선에서 각 꼭짓점 비교 
                n = array[i][j]
                if n == array[i + k][j] and n == array[i][j + k] and n == array[i + k][j + k]:
                    answer = max(answer, (k + 1) ** 2) # 기존의 answer값과 새롭게 구한 넓이를 구해서 더 큰값을 answer에 대입 
 
print(answer)

# 토너먼트
n, kim, im = map(int, input().split())
cnt = 0
while True:
    if kim == im : # 두 값이 같아지면 그때의 cnt를 세줌
        break
    kim -= kim // 2 # 두명씩 경기를 하니까 2로 나눈 몫을 구해줌
    im -= im // 2 # 두명씩 경기를 하니까 2로 나눈 몫을 구해줌
    cnt += 1

print(cnt)

# 10974 모든 순열
from itertools import permutations
n = int(input())
arr = [i for i in range(1,n+1)]
for i in list(permutations(arr, n)):
    for j in i: # 리스트 하나를 꺼내서 요소 하나씩 공백을 넣어서 출력 
        print(j, end= ' ')
    print() # 줄바꿔서 모든 리스트 & 리스트 요소 출력 함


# 7568 덩치
n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x,y])

for i in range(n):
    grade = 1 # 기본 1로 설정 
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]: # 다음값과 비교해서 다음값이 두개 다 큰 경우 +1해줌
            grade = grade + 1
    print(grade,end=" ")  # 이어서 출력


# 1436 영화감독 숌
n = int(input())
count = 0
num = 666
while True:
    if '666' in str(num): # num에 1값을 더해줘야하기때문에 기본형은 int이고 str로 바꿔서 '666'이 포함되어 있는지 확인한다.
        count += 1
    if count == n:
        print(num)
        break
    num += 1

# num을 1씩 증가시켜서 666이 문자열안에 포함되어 있다면 count를 +1 해주고
# count값과 n이 동일하다면 그때의 종말 숫자를 출력 해준다.


# 2798 블랙잭
# 플레이어는 제한된 시간안에 N장의 카드 중에서 3장의 카드를 골라야함
# 플레이어가 고른 카드의 합은 M이 넘지 않으면서 M과 최대한 가깝게 만들어야함
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오

from itertools import combinations # 중복 허용 x --> combinations
n, m = map(int, input().split()) # 카드의 개수(n) , 기준이 되는 카드의 합(m)이 주어짐
card = list(map(int, input().split()))
m_sum = 0 # max sum을 0으로 초기화 

for i in combinations(card, 3): # 카드 리스트에 있는 요소중 3개 뽑음
    card_sum = sum(i) # 3개의 i에 대한 합
    if m_sum < card_sum <= m : # max sum값이 card sum보다 작고, m(기준이 된는 합)보다 작거나 같으면
        m_sum = card_sum # max_sum에 card_sum 대입

print(m_sum)

# 2231 분해합
n = int(input())
for i in range(1, n+1): # 부르트 포스법 --> 앞에서부터 탐색함 완전탐색
    num = sum(map(int, str(i))) # i를 각 자리숫자를 문자열로 바꿔준 뒤 다시 int로 변환 후 합 계산
    n_sum = i + num # 숫자 + 각 자리수 합
    if n_sum == n:
        print(i)
        break
    if i == n: # i와 n이 같다는건 이미 실패함. 생성자 존재x (각 자리수를 더한 값도 포함이 되는데 이미 n과 같다는건 i에  각 자리수를 더했을때 값이 더 커짐 --> i는 생성자가 될 수 없음)
        print(0)

# 14501 퇴사
n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0) #뒤에 0을 추가해서 인덱스초과 오류 방지
for i in range(n - 1, -1, -1):
    if t[i] + i > n: #데드라인이 기한을 넘어가는경우
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])   # 둘중에 더 큰값으로 dp[i]값을 갱신하고 최종적으로 dp[0]의 값이 최대가된다

# 17413 단어뒤집기2
import sys
from collections import deque

stk = [] 
q=deque()
result = '' 
state = True 

S = sys.stdin.readline().rstrip()

for i in S:
    if i == "<": 
        while stk:
            result += stk.pop()  
        q.append(i) 
        state = False 
    
    elif i == ">": 
        q.append(i) 
        state = True 
        while q : 
            result += q.popleft()
    
    elif i==' ':
        if state:
            while stk:
                result += stk.pop()
            result += ' '  
        else:
            q.append(i) 
            while q: 
                result += q.popleft() #
    else: 
        if state: 
            stk.append(i) 
        else:
            q.append(i) 
while stk: 
    result += stk.pop()
print(result)