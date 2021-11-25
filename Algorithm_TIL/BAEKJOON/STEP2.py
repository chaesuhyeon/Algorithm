# 문제 번호 1330 두수 비교하기
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
A,B = map(int, input().split())
if A>B :
    print(">")
elif A<B :
    print("<")
else:
    print("==")


# 문제 번호 9498 시험성적
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
score = int(input())
if (90<= score <=100):
    print("A")
elif (80<= score <90):
    print("B")
elif (70<= score <80):
    print("C")
elif (60<= score <70):
    print("D")
else:
    print("F")


# 문제 번호 2753 윤년
# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
year = int(input())
if ((year%4 == 0 and year%100 !=0) or year%400 == 0):
    print("1")
else:
    print("0")
    

