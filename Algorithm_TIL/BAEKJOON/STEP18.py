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