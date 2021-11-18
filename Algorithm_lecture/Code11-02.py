# 선책정렬

## 함수
def selectionSort(ary) :
    n = len(ary)
    for cy in range(0, n-1) : # 사이클 개수
        minIndex = cy
        for i in range(cy+1, len(ary)):
            if (ary[minIndex] > ary[i]):
                minIndex = i
        ary[cy], ary[minIndex] = ary[minIndex], ary[cy]
    return ary

## 전역
import random
dataAry = [random.randint(1,99) for _ in range(20)]
## 메인
print('정렬 전-->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후-->', dataAry)