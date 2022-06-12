# 이분 탐색 특징
# 1. 처음과 끝을 정하고
# 2. 중간값을 구한다음
# 3. 그 중간값을 이용해 구하고자 하는것을 구하고
# 4. 처음과 끝값을 바꿔주면서 반복

import sys

n, m = map(int, sys.stdin.readline().rstrip().split()) # n : 나무의 수 / m : 나무의 길이 
h = list(map(int,sys.stdin.readline().rstrip().split())) # 나무의 높이 

start , end = 0 , max(h) # 시작값과 끝나는 값 , 끝나는 값은 높이 중에서 가장 큰 값

while start <= end :  # start가 end보다 작거나 같을 동안만 반복문 실행
    mid = (start + end) // 2 # 중앙값
    sum = 0 # 잘린 나무 합계

    for i in h : # 높이 하나씩 꺼냄
        if i > mid : # mid보다 큰 나무는 잘려나감
            sum += i - mid 

        if sum > m : # 잘린 나무 합계가 m값보다 크면 start값을 mid + 1
            start = mid + 1
        else : # 잘린 나무 합계가 m값보다 작으면 end값을 mid - 1
            end = mid - 1
    
print(end) # 값 출력 



# 시간 초과 (이분 탐색으로 안풀었음)
import sys

n, m = map(int, sys.stdin.readline().rstrip().split()) # n : 나무의 수 / m : 나무의 길이 
h = list(map(int,sys.stdin.readline().rstrip().split())) # 나무의 높이 

sum = 0
diff = 0

num=0
length = min(h)

while True :
    sum = 0

    for i in h:
        diff = i - length
        if diff < 0:
            diff = 0
        sum += diff

    if sum == m :
        print(length)
        break
    else:
        length += 1



