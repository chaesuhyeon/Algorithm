# 10829 이진수변환

N = int(input())
arr=[]
def binary_number(N):
#    print("N : ", N)
    if N == 0:
        return
    else:
        binary_number(N//2)
        arr.append(N%2)
#        print("arr : ", arr)

binary_number(N)

for i in arr:
    print(i, end='')

