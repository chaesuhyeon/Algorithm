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
import random
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
