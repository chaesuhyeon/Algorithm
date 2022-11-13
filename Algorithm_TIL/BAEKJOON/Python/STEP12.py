# 2750 수 정렬하기 
N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

num.sort()
for i in range(len(num)):
    print(num[i])
    

# 2751 수 정렬하기2
# pypy3 
N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

num.sort()
for i in range(len(num)):
    print(num[i])


# 10989 수 정렬하기3
# pypy3 
# 메모리 초과
# for문 속에서 append를 사용하면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용 하지 못함
import sys
N = int(sys.stdin.readline().rstrip())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline().rstrip()))

num.sort()
for i in range(len(num)):
    print(num[i])

# 재풀이
# python    
# 파이썬은 내부적으로 연산과 메모리를 관리하기 때문에 파이썬에 내장되어 있는 함수를 적용할 수록 메모리를 효율적으로 관리
# https://wikidocs.net/21057 참고 
# 입력값이 10000개까지 주어질 수 있는데 인덱스는 0부터 시작하므로 10001인 리스트 만듦
import sys
N = int(sys.stdin.readline())
num_list = [0] * 10001 # 리스트에 각 요소마다 0을 할당
for _ in range(N):
    num_list[int(sys.stdin.readline())] += 1 # 입력값을 받을 때마다 그 입력값과 같은 인덱스에 +1씩 해줌 

for i in range(10001):
    if num_list[i] != 0: # num_list[i]값이 0이 아니면
        for j in range(num_list[i]): # 값이 0이 아닌 것의 인덱스를 출력 
            print(i)


# 2108 통계학
import sys
N = int(sys.stdin.readline().rstrip())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
 
print(round(sum(num)/len(num))) # 산술 평균 
    
num.sort()
print(num[len(num)//2]) # 중앙값 , N은 무조건 홀수라는 조건이 있음 

# 최빈값 Counter 사용 
from collections import Counter
counter = Counter(num).most_common()
# print("counter", counter) # counter [(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)] // 원소는오름차순 & 빈도는 내림차순으로 정렬됨  
if len(counter) > 1: # num 이 1개 이상이라면 
    if counter[0][1] == counter[1][1]: # Counter의 결과가 빈도가 가장 큰 것부터 나오므로 첫번째와 두번째를 비교했을 때 같다면 두번째결과를 출력함. Counter의 결과가(두번째로 작은 숫자, 최빈값) 이므로
        print(counter[1][0])
    else: # Counter의 결과에서 첫번째와 두번째를 비교했을때 같지 않다면, 첫번째 결과값이 최빈값이 되므로 첫번째 값을 출력 
        print(counter[0][0])
else:
    print(counter[0][0]) # num의 원소가 1개라면 첫번째 값을 출력 


### 최빈값 실패. Counter 가 아닌 count()이용 
# counter = []
# count = []
# for i in range(len(num)):
#     counter.append(num.count(num[i]))
# print("conter : ", counter)
# mc = max(counter)
# print("mc 카운트 : ", counter.count(mc))
# if counter.count(mc) != 1 :
#     for i in range(len(counter)):
#         if counter[i] != mc :
#            counter.pop(i)
#         mi = counter.index(mc)
#         count.append(num[mi])
#         print("count : ", count)
#     count.sort()
#     print(count[1])

# else :
#     mi = counter.index(mc)
#     print(num[mi])     
    
print(num[-1] - num[0])  # 범위  // 이미 정렬이 되어 있으므로 인덱스로 빼줌 
    

# 1427 소트인사이드
import sys
N = list(map(int, sys.stdin.readline())) # 2413 --> [2, 4, 1, 3]
N.sort(reverse=True)
for i in range(len(N)):
    print(N[i], end='')


# 11650 좌표 정렬하기
import sys
N = int(sys.stdin.readline())
num=[]
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    num.append([x, y])

num.sort() # [[1, -1], [1, 1], [2, 2], [3, 3], [3, 4]]

for i in range(N):
    print(num[i][0], num[i][1])


# 11651 좌표 정렬하기2
import sys
N = int(sys.stdin.readline())
num=[]
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    num.append([y, x]) # y를 기준으로 정렬해야 하므로 순서 바꿔서 append 

num.sort() 

for i in range(N):
    print(num[i][1], num[i][0]) # x y 순서대로 출력을 해야하므로 [1] , [0] 으로 출력 


# 18870 좌표압축
import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

s_num = sorted(list(set(num))) # 두번째 예제 참고해서 중복값을 제거하기 위해 set함수를 사용하고 list로 바꿔준뒤 정렬

dic = dict() # 딕셔너리 생성

for i in range(len(s_num)): # 중복 제거한 원소 개수만큼 반복하여 딕셔너리에 key = value 값 저장 
    dic[s_num[i]] = i # key에 정렬된 리스트인 s_num의 원소를 넣고, 순서대로 정렬된 상태기 때문에 i값을 넣어줌   
    # 생각해보니 s_num은 정렬된 상태라 index함수를 사용할게 아니라 그냥 i로 넣어주면 됐었음..

#print(dic)  # {-10: 0, -9: 1, 2: 2, 4: 3}


for i in num:
    print(dic[i] , end= ' ') # num의 value 값을 출력 


# 1026 보물
import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()

m = 0
sum = 0
i = 0
while i < len(A):
    m = max(B) # B에서 최댓값을 뽑고
    p = B.pop(B.index(m)) # 최댓값의 인덱스를 구해서 그 인덱스의 값을 pop해서 최댓값 뽑음
    sum += A[i] * p # 그 최댓값과 A의 최솟값을 곱함
    i += 1 # 인덱스 늘려가며 A의 최솟값과 B의 최댓값을 곱해줌
print(sum) # 합계 출력 


# 2217 로프
# max_weight에서 값 * 로프의 개수(N)
import sys
N = int(sys.stdin.readline().rstrip())
rope = [0] * N 
for i in range(N):
    rope[i] = int(sys.stdin.readline().rstrip())

rope.sort(reverse=True) # 큰 값부터 계산하기 위해 

mw = 0 # max_weight
for i in range(N):
    w = rope[i] * (i+1) # rope는 한개부터 (모든 로프를 다 이용할 필요는 없으므로)
    if w > mw : # w 가 mw보다 크면 최댓값이므로 
        mw = w # w값을 mw에 대입
print(mw) # 최댓값 출력


# 11399 ATM
import sys
N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split())) # 시간 입력받음
arr.sort() # 정렬

time = [0] * N
t_sum = 0
for i in range(N):
    t_sum += arr[i] # 시간의 합계를 구해줘서
    time[i] = t_sum # time리스트에 각 사람이 걸리는 시간의 합을 넣어줌
print(sum(time)) # 리스트 전체 합 구해줌 (모든 사람의 시간의 합)


# 1764 듣보잡
import sys
N , M = map(int, sys.stdin.readline().split())
n_set = set() 
for _ in range(N):
    n_set.add(sys.stdin.readline().rstrip())

m_set = set()
for _ in range(M):
    m_set.add(sys.stdin.readline().rstrip())

result = sorted(list(n_set & m_set)) # 교집합 인것들을 list로 변환 후 정렬


print(len(result)) # 길이 출력 (듣과 보의 겹치는 것의 개수)
for i in result:
    print(i) # 겹치는 원소 출력 

# 10825 국영수
import sys
N = int(sys.stdin.readline().rstrip())
arr = [0] * N
for i in range(N):
    name, kor, eng, math = map(str,sys.stdin.readline().split())
    kor, eng, math = int(kor) , int(eng), int(math) # 점수들은 숫자로 변환
    arr[i] = [name , kor, eng, math] # 이중배열로 추가 

arr.sort(key=lambda z: (-z[1], z[2], -z[3], z[0])) # 문제에 나온 조건대로 정렬
for i in arr:
    print(i[0]) # 이름만 출력


# 3273 두 수의 합
import sys
n = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline().rstrip()) 
cnt = 0
left, right = 0, n-1

while left < right: # 왼쪽 인덱스가 오른쪽 인덱스보다 작을 경우에만 반복수행
    num = arr[left] + arr[right]
    if num == x: # x(비교값)면 cnt + 1 해주고,  작은 숫자부터 증가시켜 비교 
        cnt += 1
        left +=1
    elif num < x: # 비교값 x보다 더한값 num이 작다면 작은 숫자부터 증가시킴
        left += 1
    else: # 비교값 x보다 더한값num이 크다면 큰숫자 인덱스를 하나씩 감소시켜  비교
        right -= 1
print(cnt)


# 11656 접미사 배열
import sys
word = list(sys.stdin.readline().rstrip()) # word  :  ['b', 'a', 'e', 'k', 'j', 'o', 'o', 'n']
arr = []
tmp = "" 
for _ in range(len(word)): # 단어의 길이만큼 반복
    p = word.pop() # 맨 끝 원소 뽑음
    tmp = p + tmp # 뽑은 맨끝원소를 기존 접미사와 계속 더해줌 (순서 p먼저 주의)
    arr.append(tmp) # 합친 단어를 리스트에 append

arr.sort() # 정렬 

for i in arr: # 리스트 원소 뽑아줌
    print(i)


# 2776 암기왕
import sys
input = sys.stdin.readline


t = int(input().rstrip())

for _ in range(t):
    n1 = int(input().rstrip())
    s1 = set(list(map(int,input().rstrip().split())))
    n2 = int(input().rstrip())
    s2 = list(map(int,input().rstrip().split()))
    for i in s2:
        if i in s1:
            print(1)
        else:
            print(0)


# 1449 수리공 항공
n , l = map(int, input().split())
loc = list(map(int, input().split()))
loc.sort()

start = loc[0] # 맨 처음 값을 시작점으로
cnt = 1 # 필요한 테이프 개수 일단 1개부터 시작
for i in loc[1:]:
    if i in range(start, start+l):
        continue # 시작점 + 테이프 길이 했을 때 i의 값이 이 범위안에 들어오면 기존 테이프를 사용한다는 코드
    else: # 범위를 넘어가면 새테이프를 사용해야한다는 코드
        start = i
        cnt += 1

print(cnt)