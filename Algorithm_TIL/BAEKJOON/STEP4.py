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
#     
