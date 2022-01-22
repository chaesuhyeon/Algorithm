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

# 17478 재귀함수가 뭔가요?
# cnt변수도 사용하여 _의 반복횟수에 맞게 출력 
def recur(N, cnt):
    print("____"*cnt+"\"재귀함수가 뭔가요?\"")
    if N == 0 :
        print("____"*cnt+"\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print("____"*cnt+"라고 답변하였지.")
        return
    else:
        print("____"*cnt+"\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print("____"*cnt+"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print("____"*cnt+"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        recur(N-1, cnt+1)
        print("____"*cnt+"라고 답변하였지.")
    
N = int(input())
cnt = 0
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recur(N, cnt)

# 5568 카드 놓기
def card(depth):
    print("depth : " , depth)
    if depth == k:
        s.add(''.join(map(str, li)))
        print("s : ", s)
        return 
    for i in range(n):
        print(f'depth:{depth} & i:{i}')
        if check[i]:
            continue
        print("nums : ", nums)
        li.append(nums[i])
        print("li.append(nums[i]) : ", li)
        check[i] = 1
        card(depth+1)
        li.pop()
        print(f'depth:{depth} & li.pop():{li}')
        check[i] = 0
        
n, k = int(input()), int(input())
nums = [int(input()) for _ in range(n)]
li, s = [], set()
check = [0]*n
card(0)
print(len(s))

# 10870 피보나치수 5
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))





