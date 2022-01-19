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

# 1769 3의 배수
# 처음에 cnt를 매개변수로 안넣어줬더니 cnt집계를 잘 못함 
# cnt도 매개변수로 넣어줌
def three(N , cnt): 
    if len(N) > 1: # 숫자의 길이가 2자리수일때까지 반복문 실행 
        sum = 0
        cnt += 1
        for i in N:
            sum += int(i)
        three(str(sum), cnt)
    else: # 숫자가 한자리수이면 그 수를 3으로 나눴을 때 나머지가 0이면 3의 배수 
        if int(N) % 3 == 0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")

N = input()
cnt = 0
three(N , cnt)

