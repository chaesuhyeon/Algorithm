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


