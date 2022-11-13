# 입출력과 사칙연산

# 문제 번호 2557 
# Hello World!를 출력하시오.
print("Hello World!")

# 문제 번호 10718
# ACM-ICPC 인터넷 예선, Regional, 그리고 World Finals까지 이미 2회씩 진출해버린 kriii는 미련을 버리지 못하고 왠지 모르게 올해에도 파주 World Finals 준비 캠프에 참여했다.
# 대회를 뜰 줄 모르는 지박령 kriii를 위해서 격려의 문구를 출력해주자.
for i in (["강한친구 대한육군", "강한친구 대한육군"]):
    print(i)

print("강한친구 대한육군\n" *2)

# 문제 번호 10171
# 아래 예제와 같이 고양이를 출력하시오.
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")
# 역 슬래시일 경우 하나 더 입력해야 인식.

# 문제 번호 	10172
# 아래 예제와 같이 개를 출력하시오.
print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\__|")

# 문제 번호 	1000
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
A,B = input().split()
print(int(A)+int(B))
# A, B = input().split() : 입력되는 문자를 input()함수로 입력받고 split()함수로 나누어 각각 A,B 변수에 저장

# 문제 번호 	1001
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
A,B = input().split()
print(int(A)-int(B))

A,B = map(int, input().split()) #첫번째인자:함수, 두번째인자:데이터
print(A-B)

# 문제 번호 	10998
# 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.
A,B = input().split()
print(int(A)*int(B))

A,B = map(int, input().split()) #첫번째인자:함수, 두번째인자:데이터
print(A*B)

# 문제 번호 	1008
# 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
A,B = input().split()
print(int(A)/int(B))

A,B = map(int, input().split()) #첫번째인자:함수, 두번째인자:데이터
print(A/B)

# 문제 번호 	10869
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
A,B = map(int, input().split())
print(A+B, A-B, A*B, A//B, A%B, sep='\n')

# 문제 번호 10430
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
A,B,C = map(int, input().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')

# 문제 번호 2588
A = int(input())
D,E,F = map(str, input().split())
DEF = D + E + F
print(A*int(F),A*int(E),A*int(D), A*int(DEF) , sep='\n')
# 이방법으로 풀어서 답은 나오는데 런타임오류 난다...
# # #
A = int(input())
B = int(input()) 
out1 = A*((B%100)%10)
out2 = A*((B%100)//10)
out3 = A*(B//100)
result = A*B
print(out1, out2, out3, result, sep='\n')














