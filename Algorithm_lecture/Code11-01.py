# 최솟값 찾기

# 함수
def findMinIndex(ary) :
    minIndex = 0
    for i in range(1, len(ary)) :
        if (ary[minIndex] > ary[i]) :
            minIndex = i
    return minIndex


## 전역
testAry = [55, 88, 33, 77]

## 메인
minPos = findMinIndex(testAry)
print('최솟값-->', testAry[minPos])
