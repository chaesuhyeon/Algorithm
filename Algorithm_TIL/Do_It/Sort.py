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

# 퀵 정렬 알고리즘 구현( 원소 수가 9미만이면 단순 삽입 정렬)
from typing import MutableSequence
def sort3(a : MutableSequence , idx1 : int, idx2 : int, idx3 : int):
    """a[idx1], a[idx2] , a[idx3] 을 오름차순으로 정렬하고 중앙값의 인덱스를 반환"""
    if a[idx2] < a[idx1] : a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2] : a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1] : a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a : MutableSequence , left: int, right: int) -> None:
    """a[left] ~ a[rigth]를 단순 삽입정렬"""
    for i in range(left +1 , right + 1):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

def qsort(a : MutableSequence , left: int, right: int) -> None:
    """a[left] ~ a[rigth]를 퀵 정렬"""
    if right - left < 9:
        insertion_sort(a, left, right) # 원소수가 9이하이면 단순 삽입정렬
    else:
        pl = left # 왼쪽 커서
        pr = right # 오른쪽 커서
        m = sort3(a , pl, (pl+pr)//2 , pr) # 오름차순으로 정렬하고 중앙값의 인덱스를 반환
        x = a[m] # 피벗 값

        a[m],a[pr-1] = a[pr-1], a[m] # 중앙값(피벗)값과 끝에서 두번째 원소를 교환
        pl += 1 # a[left]의 값은 (첫번째 값은) 피벗값 이하인 값이고 
        pr -= 2  # a[right -1]과 a[right]은 피벗이상인 값이기 때문에 더이상 스캔할 필요x  [그림 6-26 참고]
        while pl <= pr:
            while a[pl] < x : pl+=1
            while a[pr] > x : pr -= 1
            if pl <= pr :
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        if left < pr :qsort(a, left, pr)
        if pl < right : qsort(a, pl, right) 

def quick_sort(a : MutableSequence) -> None:
    """ 퀵 정렬 """
    qsort(a, 0, len(a)-1)

if __name__ == "__main__":
    print('퀵 정렬을 합니다(원소 수가 9미만이면 단순 삽입 정렬을 합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    quik_sort(x)

    print('오름 차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


# 힙 정렬( = 부분 순서트리)
# 선택 정렬(최솟값 , 최댓값을 선택해 정렬하는 알고리즘)을 응용한 알고리즘
# 힙의 특성을 이용하여 정렬하는 알고리즘
# 시간 복잡도 O(n log n)
# 힙에서 최댓값은 root에 위치한다.
# 힙 : 부모의 값이 자식의 값보다 항상크다 라는 조건을 만족하는 완전 이진 트리 (부모의 값이 자식의 값보다 항상 작아도 힙 이라고 함)
# 대소관계만 일정하면 힙이라고 할 수 있음
# 형제 노드간의 대소관계는 일정하지 않음
# 트리 : 각 원소를 의미하는 노드들이 연결된 계층구조
# 완전 : 부모는 왼쪽자식부터 추가하여 모양을 유지
# 이진 : 부모가 가질 수 있는 자식의 최대 개수는 2개

# 원소a[i]에서 다음 관계가 성립 
# 부모 : a[(i-1) // 2]
# 왼쪽 자식 : a[i*2 +1]
# 오른쪽 자식 : a[i*2 + 2]

# 힙에서 최댓값인 루트를 꺼내고 루트 이외의 부분을 힙으로 만드는 과정을 반복
# 1. 루트를 꺼냄
# 2. 마지막 원소(가장 하단의 오른쪽 원소)를 루트로 이동
# 3. 루트에서 시작하여 자신보다 값이 큰 자식과 자리를 바꾸고 아래로 내려가는 작업을 반복함. 자식의 값이 작거나 리프(자식이 없는 노드. 단말노드)의 위치에 도달하면 종료

# 이 순서를 적용하기 전에 배열을 반드시 힙으로 만들어야 함
# 1. i값을 n-1로 초기화 / i : 배열의 마지막 인덱스 , n : 배열의 원소 수
# 2. a[0]과 a[i]값을 교환
# 3. a[0], a[1], ,,, a[i-1]을 힙으로 만듦
# 4. i값을 1씩 감소시켜 0이되면 종료, 그렇지 않으면 2로 돌아감

from typing import MutableSequence

def heap_sort(a : MutableSequence) -> None:
    """힙 정렬"""

    def down_heap(a : MutableSequence , left : int, right : int) -> None:
        """a[left] ~ a[right]를 힙으로 만들기"""
        temp = a[left] # 루트

        parent = left
        while parent < (right+1) // 2:
            cl = parent * 2 + 1 # 왼쪽 자식
            cr = cl + 1 # 오른쪽 자식
            child = cr if cr <= right and a[cr] > a[cl] else cl # 큰 값을 선택
            if temp  >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp
    
    n = len(a)

    for i in range((n-1)//2 , -1, -1): # a[i] ~ a[n-1]을 힙으로 만들기
        down_heap(a, i, n-1)
    
    for i in range(n-1, 0, -1):
        a[0] , a[i] = a[i], a[0] # 최댓값인 a[0]과 마지막 원소를 교환
        down_heap(a, 0, i-1) # a[0] ~a[i-1]을 힙으로 만들기

    
if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))
    
    heap_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# heap_sort()함수는 원소수가 n인 배열a를 정렬하는 함수
# 1단계 : down_heap()함수를 호출하여 배열 a를 힙으로 만듦
# 2단계 : 최댓값인 루트 a[0]을 꺼내서 배열의 마지막 원소와 교환하고 배열의 남은 부분을 다시 힙으로 만드는 과정을 반복하여 정렬을 수행

# 파이썬의 heapq모듈
# 힙에 원소를 추가하는 heappush()
# 힙에서 원소를 제거하는 heappoop() 함수
# 이때 푸시와 팝은 힙의 조건을 유지하며 수행

import heapq
from typing import MutableSequence

def heap_sort(a : MutableSequence) -> None:
    """힙 정렬(heapq.push와 heapq.pop을 사용)"""
    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)

    # ... 생략


# 계수 정렬
# 특정 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 알고리즘
# 계수 정렬은 데이터 크기 범위가 제한되어 정수형태로 표현할 수 있을 때 사용 가능
# 원소의 대소관계를 파악하지 않음
# 데이터의 개수가 N, 데이터(양수)중 최댓값이 K일때 최악의 경우에도 수행시간 O(N+K)를 보장
# 공간 복잡도도 O(N+K)
# 동일한 값을 가지는 데이터가 여러개 등장할 때 효과적으로 사용할 수 있음
# 성적의 경우 100점을 맞은 학생이 여러명일 수 있기 때문에 계수 정렬이 효과적임



# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
    
for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end = ' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력



        


