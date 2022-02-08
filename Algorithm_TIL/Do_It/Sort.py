# 선택 정렬
# 맨 첫번째 값을 제일 작은 값이라고 가정하고 진행

# 최솟값 구하기
def findMinIndex(ary):
    minIndex = 0
    for i in range(1, len(ary)):
        if (ary[minIndex] > ary[i]):
            minIndex = i
    return minIndex

testAry = [55,88,33,77]
minPos = findMinIndex(testAry) # index 반환
print('최솟값 --> ', testAry[minPos])

## 정렬까지
# 이 방법은 리스트 두개를 사용하므로 개선된 방법이 필요함 
from cmath import pi
import random
from turtle import right
before = [random.randint(1, 99) for _ in range(20)] # 1~99까지 20개 랜덤하게 숫자 생성
after=[]
print('정렬 전 ---> ', before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후 ---> ', after)

# 개선된 방법 : 사이클 이용 (제일 작은 값을 맨 앞으로 보내고, 그 값을 제외한 다른 값들과 또 비교해서 제일 작은 값을 맨 앞으로 보냄 )
# 사이클 : 개수 - 1번 실행
def selectionSort(ary):
    n = len(ary)
    for cy in range(0, n-1):
        minIndex = cy
        for i in range(cy+1, len(ary)):
            if (ary[minIndex] > ary[i]):
                minIndex = i
        ary[cy], ary[minIndex] = ary[minIndex], ary[cy]       
        
    return ary

import random
dataAry = [random.randint(1, 99) for _ in range(20)] # 1~99까지 20개 랜덤하게 숫자 생성

print('정렬 전 --> ' , dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 --> ' , dataAry)

# 삽입정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입하는 정렬
# 현재 리스트의 데이터가 거의 정렬된 상태라면 매우 빠르게 동작
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array)):
    for j in range(i,0,-1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1] : # 한칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤 
            break
print(array)


# 퀵 정렬
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 가장 기본적인 퀵 정렬은 첫번째 데이터를 기준 데이터(Pivot)로 설정
# 퀵정렬은 평균의 경우 O(NllogN)의 시간 복잡도를 가짐 but 최악의 경우 O(N^2)의 시간 복잡도를 가짐
# 표준 라이브러리를 이용한 경우에는 O(NllogN)의 시간 복잡도를 보장해주지만, 직접 첫번째 원소를 피벗으로 삼는 경우 O(N^2)의 시간복잡도가 나올 수 있음
# 재귀적으로 수행

array = [5,7,9,0,3,1,6,2,4,8]
def quik_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right) :
        #
        #  피벗보다 큰 데이터를 찾을 때 까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while(right > start and array[right] >=  array[pivot]):
            right -= 1

        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right] 
        else : # 엇갈리지 않았다면 작은데이터와 큰 데이터를 교체
            array[left] , array[right] = array[right], array[left]

    quik_sort(array, start, right-1)
    quik_sort(array, right+1, end)

quik_sort(array, 0, len(array)-1)
print(array)

# 위의 코드를 더 간단하게
array = [5,7,9,0,3,1,6,2,4,8]
def quik_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]# 분할된 왼쪽 부분 /  피벗을 제외한 리스트에 각 원소를 하나씩 확인하면서 피벗값보다 작은 경우에는 왼쪽 리스트에 담길 수 있도록 함
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분 / 피벗을 제외한 리스트에 각 원소를 하나씩 확인하면서 피벗값보다 큰 경우에는 오른쪽 리스트에 담길 수 있도록 함

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quik_sort(left_side) + [pivot] + quik_sort(right_side)
print(quik_sort(array))

# do_it 코드, 배열을 두 그룹으로 나누기
# 배열 가운데 위치한 원소를 피벗으로 선택함
# 피벗을 어떤 값으로 선택하느냐에 따라 배열을 나누는 것과 정렬 성능에 영향을 미침 
from typing import MutableSequence
def partition(a : MutableSequence) -> None:
    """배열을 나누어 출력"""
    n = len(a)
    pl = 0 # 왼쪽 커서
    pr = n-1 # 오른쪽 커서
    x = a[n//2] # 피벗 (가운데 원소)

    while pl <= pr:
        while a[pl] < x : pl +=1
        while a[pr] > x : pr -=1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'피벗은 {x}입니다.')
    print(f'피벗 이하인 그룹입니다.')
    print(*a[0 : pl]) # a[0]~ a[pl-1]

    if pl > pr +1 :
        print(f'피벗 일치하는 그룹입니다.')
        print(*a[pr + 1 : pl]) # a[pr+1]~ a[pl-1]

    print(f'피벗 이상인 그룹입니다.')
    print(*a[pr+1 : n]) # a[pr+1]~ a[n-1]

if __name__ == '__main__':
    print("배열을 나눕니다.")
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    partition(x)








        


