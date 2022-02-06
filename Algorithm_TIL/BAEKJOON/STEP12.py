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

