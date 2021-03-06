# 스택

# 문제 번호 10828 스택 
import sys
stk =[]

N = int(sys.stdin.readline())

for _ in range(N):
    menu = sys.stdin.readline().split()
    
    if menu[0] == "push" :
        stk.append(menu[1]) # 2번째 index에 있는 값 삽입
    
    elif menu[0] == "pop" :
        if len(stk) == 0:
            print(-1)
        else :
            print(stk.pop())
            
    elif menu[0] == "size" :
        print(len(stk))
        
    elif menu[0] == "empty" :
        if len(stk) == 0:
            print(1)
        else :
            print(0)
            
    elif menu[0] == "top" :
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])  
            

# 문제 번호 10773 제로
import sys

K = int(sys.stdin.readline())
stk = []

for k in range(K):
    num = int(sys.stdin.readline())
    if num == 0: # 입력 받은 숫자가 0일 경우
        if len(stk) == 0: #  예외 처리를 안해주면 처음 입력 받은 숫자가 0일 경우 뺄 숫자가 없어서 index error 발생   
            try :
                continue  # 오류 발생하면 그냥 반복문 처음부터 진행
            except :
                IndexError
        else:
            stk.pop() # 빈 리스트가 아니라면 , 마지막 단어 pop해줌
    else:
        stk.append(num) # 입력 받은 숫자가 0이 아닐 경우 그냥 리스트에 추가해줌
print(sum(stk)) # 리스트 각 요소의 합 출력



# 처음에는 다 입력 받아서 리스트 먼저 생성 후 index 거꾸로 하면서 체크해주는 방법.. 근데 0이 또 나올 경우를 코드 못짜겠음..

# for k in range(1, K+1):
#     num = int(sys.stdin.readline())
#     stk.append(num)

# for i in range(K, 1, -1):
#     if stk[i] == 0 :
#         if stk[i-1] != 0:
#             stk.pop(stk[i-1])
#         else:
#             if stk[i-2] !=0:
#                 stk.pop(stk[i-2])
#     else :
#         continue



# 문제 번호 9012 괄호 

# 리스트가 빈 경우에 )가 나오면 계속 오류가 발생해서 
# try문을 써줬는데 예외 처리를 해주면 계속 빈리스트여서 결국 리스트 길이0이됨.. 
# 그렇게 되면 올바른 괄호 처리가 돼서 15~18라인 부분만 풀이참고..

# 리스트가 빈 경우에 )가 나오면 계속 오류가 발생해서 
# try문을 써줬는데 예외 처리를 해주면 계속 빈리스트여서 결국 리스트 길이0이됨.. 
# 그렇게 되면 올바른 괄호 처리가 돼서 15~18라인 부분만 풀이참고..

import sys
T = int(sys.stdin.readline())
for t in range(T):
    ps = sys.stdin.readline()
    stk =[]

    for i in ps:
        if i == "(": # 문자열 하나씩 for문 돌려서 보는데 i 가 ( 라면 리스트 stk에 추가한다
            stk.append(i)
        elif i == ")": # i 가 ( 일 경우에 , 리스트가 빈 리스트가 아니고, 리스트의 마지막 원소값이 ( 일경우에 pop해줌 
            if len(stk) != 0 and stk[-1] == "(":
                stk.pop()
            else: # len(stk) == 0 and stk[-1] == ")" 일 경우에는 어차피 빈 리스트에 원소가 )라는 말은 올바른 괄호가 아니라는 말
                stk.append(i) # 추가를 해줘서 빈 리스트가 아니도록 만듦 (어차피 올바른 괄호가 아니라서)

    if len(stk) == 0 :
        print("YES")

    elif len(stk) > 0:
        print("NO")

# 문제 번호 4949 균형잡힌 세상 
        
import sys

while True: # 반복 횟수가 정해지지 않아서 while문 사용
    sentance = sys.stdin.readline()
    stk = []
    if sentance[0] == ".": # 첫번째 문자로 .이 들어오면 반복문 종료
        break
    for i in range(len(sentance)):
        if (sentance[i] == "(") or (sentance[i] == "[") : # ( 거나 [이면 리스트 stk에 추가 
            stk.append(sentance[i])
            # print("append : ", stk)
        elif (sentance[i] == ")"): # )이면 
            if len(stk) != 0 and (stk[-1] == "(") : # 빈 리스트가 아니고, 리스트의 마지막 원소가 ( 일때 ( pop 해줌
                stk.pop()
                # print("pop : ", stk)
            else :  # stk가 빈 리스트라면 
                stk.append(sentance[i]) # )를 추가해준다. 어차피 )가 먼저 추가되므로 올바른 균형이 아니므로 바로 반복문 종료시킴
                break
        elif (sentance[i] == "]"): # )와 같은 원리
            if len(stk) != 0 and (stk[-1] == "[") :
                stk.pop()
                # print("pop : ", stk)
            else:
                stk.append(sentance[i])
                break 

    if len(stk) == 0: # 빈 리스트면 다 pop돼서 균형이 잡혔다는 뜻으로 올바른 균형
        print("yes")
    elif len(stk) > 0: # 0 이상이라면 , 모두 pop되지 않아 균형잡힌 문장이 아님을 판단
        print("no")
    i+=1 # i를 증가시켜 반복 계속 진행

# 문제 번호 1874 스택 수열

import sys

n = int(sys.stdin.readline())
arr = []
sign=[]
cnt = 1
for i in range(n):
    num = int(sys.stdin.readline())
    while cnt <= num: # 숫자는 1부터니까  입력 들어온 숫자까지 반복문 돌려가며 리스트에 append해줌 
        arr.append(cnt)
        sign.append("+")
        cnt += 1
    if arr[-1] == num:
        arr.pop()
        sign.append("-")
    else:
        sign.append("NO")
        
if "NO" not in sign: # sign리스트에 NO가 없으면 그대로 부호만 출력
    for s in sign:
        print(s)
else:
    print("NO") # NO가 있다면 NO출력
    
# 문제 번호 1406 에디터
import sys
stk1 = list(sys.stdin.readline().rstrip())
stk2 = []
M = int(sys.stdin.readline())
for i in range(M):
    menu = sys.stdin.readline().split()
    if menu[0] == "L":
        if stk1 :
            stk2.append(stk1.pop())
        else :
            continue

    elif menu[0] == "D":
        if stk2 :
            stk1.append(stk2.pop())
        else:
            continue
    elif menu[0] == "B":
        if stk1:
            stk1.pop()
        else :
            continue
    elif menu[0] == "P":
        stk1.append(menu[1])

print(''.join(stk1 + list(reversed(stk2))))


# 문제 번호 1935 후위표기식2 

import sys    
N = int(sys.stdin.readline()) # 피연산자 개수 
arr = list(sys.stdin.readline().rstrip()) # 입력받은 문자열
stk = []
num= []

for i in range(N) :
    num.append(input()) # 숫자 입력 (예제처럼) 해서 num 리스트에 추가 

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(arr)) : # 입력받은 문자열 길이만큼 반복
    if arr[i].isalpha() : # 만약에 문자 한개가 알파벳이라면 
        arr[i] = num[alpha.index(arr[i])] # alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'에서 arr[i](문자)의 index를 찾고 리스트 num에서 index에 맞는 숫자를 반환하여 문자를 숫자로 치환 

for i in arr : # 문자열에서 하나씩 꺼냄 
    if i.isdigit() : # 문자가 숫자로 되어 있다면 
        stk.append(i) # 스택에 추가 

    else: # 문자열이 숫자가 아니라면
        m = float(stk.pop())
        n = float(stk.pop())
        if i == '+' :
            stk.append(n+m)
        elif i == '-' :
            stk.append(n-m)
        elif i == '*' :
            stk.append(n*m)
        elif i == '/' :
            stk.append(n/m)

print("%0.2f" % (stk[0])) # 소숫점 둘째짜리까지 / 최종적으로 stk에는 결과값이 1개있을 것이므로 stk[0]을 소숫점 둘째자리까지 출력    
  
  
# 2257 화학식량
import sys
ch = list(sys.stdin.readline().rstrip())

c = { "H" : 1, "C" : 12, "O" : 16 }

stk=[]

for i in ch:
    if i in c:
        stk.append(c[i]) # 문자 i가 딕셔너리 c에 포함되어 있다면, i의 키값을 stk에 append 
    elif i == "(":
        stk.append(i)
    elif i == ")": # ")"가 나오면 "("가 나올때까지 pop해서 그 숫자들의 누적합을 구해서 stk에 append (15~23행)
        add = 0
        while True:
            a = stk.pop()
            if a == "(": 
                break
            add += a
        if add == 0:
            continue
        else:
            stk.append(add)
    else:
        num = stk.pop() # 문자지만 , 숫자가 나오면 stk의 최근 데이터를 pop해서 그 숫자와 곱해줌 
        add = num * int(i) # i는 보기에는 숫자지만 문자이므로 int로 바꿔줌
        stk.append(add) # 합을 stk에 append해줌 
print(sum(stk)) # stk의 합을 계산  


# 3986 좋은 단어
import sys
N = int(sys.stdin.readline())

stk = []
cnt = 0 # 좋은 단어 아닌 것 개수 
for _ in range(N): 
    stk = [] # stk 초기화 
    alpha = sys.stdin.readline().rstrip() # 단어 입력 받음 
    for i in alpha:
        if len(stk) == 0: # stk이 빈리스트면 stk에 append해줌  
            stk.append(i)

        else:  # 빈 리스트가 아닐 경우  
            if i == stk[-1]: # i와 stk마지막 문자가 같으면 
                stk.pop() # 마지막 문자를 pop해서 stk에서 제거 해줌
            elif i != stk[-1]: # i와 stk마지막 문자가 다르면 ex) stk = ['A']인데 i = 'B' 일 경우
                stk.append(i) # stk에 추가해줌 
    if len(stk) != 0: # 반복문을 다 돌았을때 stk가 빈문자열이 아니라면 삭제되지않은 문자가 있다는 뜻 (쌍이 맞지않은 문자 존재)
        cnt += 1 # +1 카운트 해줌 
print(N - cnt) # 최종적으로 전체 단어 개수(N)에서 좋은 단어가 아닌 것 개수(cnt)를 빼줌

# 문제 번호 5397 키로거
# 1406 에디터 문제와 같은 방법으로 풀었음  근데 시간 1560ms..
import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    stk1 = []
    stk2=[]
    pwd = list(sys.stdin.readline().rstrip())
    for i in pwd: # 입력받은 문자열이 
        if i.isalpha(): # 알파벳이면 stk1에 append
            stk1.append(i) 
        elif i.isdigit(): # 문자인 숫자면 
            stk1.append(i) # stk1에 append
        elif i == "<": # 왼쪽으로 커서 이동하는 경우 
            if len(stk1) > 0: #  # 왼쪽 스택이 빈 리스트가 아니라면 
                stk2.append(stk1.pop()) # 마지막 문자를  pop 해줘서 두번째 스택으로 이동
            else: # 빈 리스트트면
                continue # 무시하고 위로 올라가 반복 수행 
        elif i == ">": # 오른쪽으로 커서 이동하는 경우 
            if len(stk2) > 0: #스택이 빈 리스트가 아니라면
                stk1.append(stk2.pop()) # # 마지막 문자를  pop 해줘서 두번째 스택으로 이동
            else: # 빈 리스트트면
                continue # 무시하고 위로 올라가 반복 수행 
        elif i == "-": # 백스페이스일 경우 &  stk1이 빈 리스트가 아닌 경우  앞 문자 삭제 
            if len(stk1) > 0:
                stk1.pop()  # 왜 stk1에서 마지막 문자를 빼주냐면 백스페이스는 무조건 문자뒤에 올거라고 가정.. 문자 추가는 첫번째 스택 stk1에서 진행되기 때문에 첫번째 스택에서 pop해줌 
            else:
                continue
    print(''.join(stk1 + list(reversed(stk2))))
    

# 문제 번호 10799 쇠막대기 
# 문제 풀이방법을 전혀 생각 못해서 아이디어 참고..
# (가 나오면 stack에 push
# )가 나올 경우 그 전 문자열이 (일 경우 stack에서 pop해주고 스택 크기만큼 result에 더함
# 그 전 문자열이 )일 경우 stack에서 pop하고 result에 1을 증가 시킴

import sys
ps = sys.stdin.readline().rstrip()
stk = []
result = 0

for i in range(len(ps)):
    if ps[i] == "(":
        stk.append("(")
    else: # ")"경우
        if ps[i-1] == "(":
            stk.pop()
            result += len(stk)
        else:
            stk.pop()
            result += 1
print(result)
    

# 문제 번호 11899 괄호 끼워넣기
import sys
S = sys.stdin.readline().rstrip()

stk1 = [] # "("만 담는 스택
stk2=[] # ")"만 담는 스택 

for i in S: # 문자열 하나하나 반복문 돌려봄 
    if i == "(":
        stk1.append("(") # 여는 괄호이면 stk1에 append
    else: # 닫는 괄호이면 
        if stk1: # stk1이 빈 리스트가 아니라면 (stk1이 빈 리스트일 경우에는 pop실행x )    
            stk1.pop()
        else: # stk1가 빈 리스트가 아니면 여는 괄호가 없다는 뜻이기 때문에 여는괄호 필요함 -> 개수 측정해 주기위해 stk2에 append
            stk2.append(")")
print(len(stk2)+len(stk1)) # 없애지 못한 각 괄호들의 개수를 구해줌 (짝이 필요한 괄호들의 개수)    


# 문제 번호 12605 단어순서 뒤집기
import sys
N = int(sys.stdin.readline())
stk = []
cnt = 0

for _ in range(N):
    stk = [] # word를 append 하기전 stk 초기화 
    word = sys.stdin.readline().split() # 공백으로 split
    for _ in range(len(word)): # 입력한 문자의 길이 만큼 반복 
        stk.append(word.pop()) # word에서 하나씩 pop해서 stk에 append

    cnt += 1 # case 번호 1번부터 출력하기 위해서 
    print(f'Case #{cnt}: ' , end='') # end 써서 이어서 출력 
    for j in range(len(stk)): # stk에 담겨진 문자열 하나하나 뽑아서 end 써서 이어서 출력 
        print(stk[j], end=' ')
    print() # case 한개의 출력이 끝나면 줄바꿈 

# 문제 번호 12789 도키도키 간식드리미
from collections import deque
n = int(input())
num = deque(map(int, input().split()))
stk = deque([])
cnt = 1
while num :
    if num[0] == cnt: # 첫번째 숫자가 cnt와 같으면 pop해줌
        num.popleft()
        cnt += 1
    else:
        stk.append(num.popleft()) # cnt와 같지 않으면 빼주고 스택에 append
    
    while stk: # 스택이 존재한다면
        if stk[-1] == cnt: # 스택의 마지막 데이터와 cnt가 같으면 stk에서 제거 
            stk.pop()
            cnt+=1
        else: # 다 제거되면 반복문 종료 
            break
if len(stk) == 0:
    print('Nice')
else:
    print('Sad')


# 문제 번호 14713 앵무새

# 문제 번호 15815 천재수학자 성필 
# 후위표기식2와 같은 방법으로 풀이함 
import sys
num = sys.stdin.readline().rstrip()
stk = []
for i in num:
    if i.isdigit():
        stk.append(int(i))
    else:
        n1 = stk.pop()
        n2 = stk.pop()        
        if i == "*":
            stk.append(n2 * n1)

        elif i == "/":
            stk.append(n2 // n1)  # 문제에서 모든 계산 결과가 정수라고 명시되어 있기 때문에 /가 아닌 //로 써줌 

        elif i == "+":
            stk.append(n2 + n1)

        else:           
            stk.append(n2 - n1)
            
print(stk[0])    

# 문제 번호 17413 단어 뒤집기 2
import sys
from collections import deque

stk = [] ## 괄호 밖 문자 저장 
q=deque() ## 괄호 안의 문자
result = '' ## 총 결과값
state = True ## true = 뒤집어서 출력 / false : 안뒤집음

S = sys.stdin.readline().rstrip()

for i in S:
    if i == "<": # "<" 괄호가 나올때
        while stk: # 만약 괄호 밖의 문자가 존재한다면
            result += stk.pop() # 현재 있는 결과에 거꾸로 출력 
        q.append(i) # "<" 괄호 큐에 append
        state = False # 괄호 안이라는 상태표시. 뒤집을 필요 없는 상태
    
    elif i == ">": # ">" 괄호가 나오면
        q.append(i) # 큐에 닫는 괄호 append
        state = True # 괄호가 끝났기 때문에 다시 뒤집을 필요가 있다는 상태표시를 해줌
        while q : # 괄호부터 괄호 안에있는 문자를 결과값에 저장
            result += q.popleft() # popleft()를 이용하여 왼쪽부터 pop
    
    elif i==' ': # i가 공백문자라면
        if state: # 괄호 밖일 때 (state = True)
            while stk: # 스택이 존재할때까지  
                result += stk.pop() # 이제까지 스택에 저장된 문자들을 pop해줘서 거꾸로 만들어주고 결과값에 저장
            result += ' '  # 문자를 뒤집어서 출력해준 뒤 결과값에 공백 추가 
        else: # 괄호 안이라면
            q.append(i) # 그냥 공백문자 추가해줌
            while q: # 큐가 존재한다면 존재하는 동안 result에 문자 저장 
                result += q.popleft() #
    else: # i가 괄호, 공백이 아닌 문자일때
        if state: # 만약 괄호 밖이라면 (state = True)
            stk.append(i) # 스택에 추가해줌 
        else: # 괄호 안이라면
            q.append(i) # 큐에 추가해줌
while stk: # 혹시 스택에 남아있는 문자가 있다면 (마지막이 문자라면 추가만 될 뿐 pop해서 빼주는 과정이 빠졌기 때문에 pop해준다)
    result += stk.pop() # 모두 결과값에 저장
 
print(result) # 최종 결과 출력 



# 문제 번호 17608 막대기
import sys

N = int(sys.stdin.readline().rstrip()) # 막대기의 수 
stk =[]
num = []
for _ in range(N): # 막대기의 수 만큼 반복
    num.append(int(sys.stdin.readline().rstrip())) # 입력 받은 막대기의 높이를 리스트에 추가 

stk.append(num[-1]) # stk에 젤 오른쪽 막대기 높이 삽입

for i in range(len(num)): # 막대기 개수만큼 반복함
    p = num.pop() # 오른쪽 막대기부터 봐야하므로 pop해서 막대기 높이 비교함
    if p > stk[-1]: # pop한 막대기가 stk에 추가된 막대기보다 높은 높이라면 
        stk.append(p) # stk에 추가해줌 
print(len(stk)) # 스택의 길이 (막대기의 개수)

    

# 문제 번호 17952 과제는 끝나지 않아!
import sys
N = int(sys.stdin.readline().rstrip())
stk = []
sum = 0

for _ in range(N):
    hw= list(map(int, sys.stdin.readline().rstrip().split())) # 과제 정보 입력 

    if hw[0] == 1: # 과제가 존재한다면 
        stk.append([hw[1], hw[2]]) # 점수와 시간만 스택에 추가해줘서 2차원 리스트로 만듦
        print("stk : " , stk)

    if stk: # 숫자가 1이든 0이든 과제의 시간은 감소해야하기 때문에 이렇게 작성 / 스택이 존재한다면 ~ 
        stk[-1][1] -= 1 # 시간 1분 감소 
        print("stk time -1 : " , stk)
        if stk[-1][1] == 0: # 시간이 0분이 되면 점수를 추가해주고 스택에서 빼줌 
            sum += stk[-1][0] 
            stk.pop()
            print("stk pop : ", stk)
        else:
           pass
    else:
        pass           
print(sum) # 최종적으로 더해진 점수 출력     


# 문제 번호 23253 자료구조는 정말 최고야 
# 막대기 문제랑 비슷한 것 같다.
# 내림차순 아이디어 얻고 스택으로 다시 풀이 
# 모든 더미가 내림차순으로 정렬이 되어 있는 상태여야함

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())

status = True # 상태 체크를 위한 변수 

for _ in range(M):
    stk = [] # 스택 초기화 
    num = sys.stdin.readline() # 한 더미의 책 개수 
    book= list(map(int, sys.stdin.readline().rstrip().split())) # 책 번호 입력 
    
    while book: # 책이 존재하는 동안 
        for i in range(len(book)): # 책의 개수만큼 반복 
            if stk: # 만약에 스택이 존재한다면 
           
                if stk[-1] < book[-1]: # 스택의 마지막 데이터와 책의 마지막 데이터를 비교했을 때 책의 번호가 더 크다면 pop 해줌 
                    stk.append(book.pop()) # 스택에 append해줌
                
                else: # 만약에 스택에 있는 책 번호가 더 크다면 정렬실패 
                    status = False # 실패했으니 상태 false
                 
            else: # 빈 스택이라면 데이터 추가 (맨처음에는 스택이 비어있기 때문에 데이터 넣어줘야함)
                stk.append(book.pop())
                
        if status == False: # for문을 다 돌았는데 상태가 여전히 false라는 것은 정렬에 실패했다는 것
            break # 반복문 더 진행할 필요가 없음(뒤에 숫자(책번호)가 더 남았을 경우에 해당)
   
    if status == False: # while문이 종료됐는데 상태가 false라면 내림차순이 안되는 부분이 있었다는 뜻
        continue

if status == True: # 반복문 다 끝났는데 false가 한부분도 없어서 다 true가 나왔다면 yes
    print("Yes")
else : # false가 나왔다는건 더미 중 내림차순이 아닌 더미가 있었다는 뜻이므로 no
    print("No")





























