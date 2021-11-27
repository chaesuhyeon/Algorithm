# for 문 
# 문제번호 2739 구구단
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.

N = int(input())

for n in range(1,10):
    print(N, "*", n, "=", N*n)


# 문제 번호 10950 A + B -3
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

T = int(input())

for _ in range(T):
    A,B = map(int, input().split())
    print(A+B)


# 문제 번호 8393 합
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())
sum=0
for i in range(1,n+1):
    sum += i
print(sum)


# 문제 번호 15552 빠른 A+B
# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

import sys
 
T = int(input())
for i in range(T):
        A,B = map(int, sys.stdin.readline().split())
        print(A+B)


# 문제 번호 2741 N찍기
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

N = int(input())
for i in range(1,N+1):
    print(i) 
    

# 문제 번호 2742 기찍 N
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# 이 방법은 틀림 -> 답은 나오는데 알고리즘 제출에선 틀림,,,
N = int(input())
for i in reversed(range(1,N)):
    print(i)

# 이 방법은 맞음
N = int(input())
for i in range(N,0,-1):
    print(i)


# 문제 번호 11021 A+B - 7
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

T = int(input())
x = 0
for _ in range(T):
    A,B = map(int, input().split())
    x = x + 1
    print("Case #" + str(x) + ":",A+B)


# 문제 번호 11022 A+B - 8
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

T = int(input())
x = 0
for _ in range(T):
    A,B = map(int, input().split())
    x = x + 1
    print("Case #" + str(x) + ":", A,"+",B,"=",A+B)



# 문제 번호 2438 별 찍기 -1
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# *
# **
# ***
# ****
# *****
N = int(input())
for i in range(1, N+1):
    print("*" * i)


# 문제 번호 2439 별 찍기 -2
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제 . 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.   
N = int(input())
for i in range(1, N+1):
    print(" " * (N-i) + "*" * i)


# 문제 번호 10871 x보다 작은 수 
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
N,X = map(int, input().split())
num = list(map(int, input().split()))
for i in range(N):
    if num[i] < X:
        print(num[i], end=" ")  # end = " " 로 한칸씩 띄어서 출력

    