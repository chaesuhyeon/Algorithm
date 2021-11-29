# while문

# 문제 번호 10952  A+B -5
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

while True:
    A,B = map(int, input().split())
    if A  == 0 and B == 0:
        break
    if A != 0 and B != 0:
        print(A+B)


    
# 문제 번호 10951 A + B -4
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
count = 0
while count < 5:
    A,B = map(int, input().split())
    print(A+B)
    print(count)
    count += 1

# 테스트 개수가 주어지지 않았을 때 사용  

while True:
    try:
            A,B = map(int, input().split())
            print(A+B)
    except:
        break
    

# 문제 번호 1110 더하기 사이클
#  0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
#  먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
#  그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다

A= int(input())
num = A
count = 0
while True:
    a = num // 10
    b = num % 10
    c = (a+b) % 10
    num = (b * 10) + c
    
    count +=1
    if(num == A):
        break
print(count)
      

    
