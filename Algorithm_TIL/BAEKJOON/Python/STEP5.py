# 1차원 배열 

# 문제 번호 10818 최소, 최대
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

N = int(input())
a  = list(map(int, input().split()))
max_a = max(a)
min_a = min(a)
print(min_a, max_a)

# 문제 번호 2562 최댓값
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

b = []
for i in range(9):
    b.append(int(input()))
max_b = max(b)
print(max_b)
print( b.index(max_b)+1)


# 문제 번호 2577 숫자의 개수 
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

List = []
for i in range(3):
    List.append(int(input()))
a = str(List[0] * List[1] * List[2])
print(a.count("0"),a.count("1"), a.count("2"), a.count("3"), a.count("4"), a.count("5"), a.count("6"), a.count("7"), a.count("8"), a.count("9"), sep="\n")

#
a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))
    
# 문제 번호 3052 나머지
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
#수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

a = []
b = []
for i in range(10):
    a.append(int(input()))
    b.append(a[i] % 42)
c = set(b)
print(len(c))


# 문제 번호 1546 평균
# 새로운 평균을 구하는 프로그램을 작성하시오.

N = int(input())
a = []
a = list(map(int, input().split()))
max_a = max(a)
score = []
for i in range(N):
    score.append(a[i]/max_a * 100)
print(sum(score)/N) 
    
    
# 문제 번호 8958 ox퀴즈
n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0  
    sum_score = 0 
    for ox in ox_list:
        if ox == 'O':
            score += 1 
            sum_score += score
        else:
            score = 0
    print(sum_score)
                    

# 문제 번호 4344 평균은 넘겠지
n = int(input())
a = []

for i in range(n):
    a = list(map(int, input().split()))
    avg = sum(a[1:])/a[0]
    student = 0
    for score in a[1:]:
        if score > avg :
            student +=1
    rate = student / a[0] * 100
    print(f'{rate:.3f}%')
    
    
    
    





