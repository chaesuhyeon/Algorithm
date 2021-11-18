#이진 검색 알고리즘


## 함수
def binarySearch(ary, fdata) :
    pos = -1
    start = 0
    end = len(ary) - 1
    while (start <= end) :
        mid = (start + end) // 2
        if (ary[mid] == fdata) :
            return mid
        elif fdata > ary[mid] :
            start = mid + 1
        else :
            end = mid - 1
    return pos


## 전역
dataAry = [50,60,105,120,150,160,162,168,177,188]
findData = 164 # 할머니키


## 메인
print('배열-->', dataAry)
position = binarySearch(dataAry, findData)
if position == -1 :
    print(findData, '가 없어요ㅠ')
else :
    print(findData, '가', position, '위치에 있음 ^^')
​