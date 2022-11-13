# 문자열

# 문제 번호 11654 아스키 코드
# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

# 파이썬에서 문자를 아스키 코드로 바꾸는 방법
# ord(문자) : 아스키 코드를 반환
# chr(숫자) : 숫자에 맞는 아스키 코드를 반환

word = input()

print(ord(word))



# 문제 번호 11720 숫자의 합 
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
N = int(input())
number = list(input())
result = 0
for i in range(N):
    result += int(number[i])
print(result)
    

# 문제 번호 10809 알파벳 찾기
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
S = input()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')


# 문제 번호 2675 문자열 반복
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
T = int(input()) # 테스트 케이스 개수
for i in range(1,T+1):
    R,S = map(str, input().split()) # 반복횟수와 문자열 입력
    R = int(R) # 반복횟수를 정수로 바꿔줌
    P = "" # 새로운 문자열 P를 빈문자열로 생성
    for s in range(len(S)): # 문자열 길이만큼 반복
        P += S[s]*R # 문자열 각 인덱스에 R만큼(반복횟수) 곱해줌
    print(P)
        
    
# 문제 번호 1157 단어 공부
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
S = input().upper() # 입력받고, 대문자로 바꿔줌
sarray = list(set(S)) # 일단 중복값 제거
array = []

for s in sarray:
    array.append(S.count(s)) # 문자열 S에서 s의 개수를 array에 추가 
mc = max(array) # 배열 array에서 max값  count(개수) 구하기 
if array.count(mc) != 1: # max count의 개수가 1이 아니면 max값이 더 있다는 것  
    print("?")
else:
    mi = array.index(mc) # max값개수가 1이면 array배열에서 max값이 있는 index찾아서 mi에 저장 max index
    print(sarray[mi]) # array 인덱스와 sarray가 같기 때문에 max값 인덱스번째 값을 찾음 

# 처음 생각했던 값인데, 중복값 제거를 못해서 헤맸음
#S = input()
#array = []
#S = S.upper() # 대문자로 바꿔줌
#for i in range(len(S)):    
#    array.append(S.count(S[i]))
#    print("array : ",array)
#    mc = max(array)
#    print("mc : ",mc)
#    if array.count(mc) != 1:
#        print("?")
#    else:
#        mi = array.index(mc)
#        print(S[mi])    



# 문제 번호 1152 단어의 개수
# 첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.
S = input().split()
print(len(S))

# 단어의 개수는 공백개수 + 1 개(앞뒤로 공백이 없을 때) //실패 
#S = str(input())
#count = 0 
#for i in range(len(S)):
#    if S[i] == " ":
#        if S[0] == " " :
#            count -= 1
#        elif S[len(S)-1] ==" ":
#            count -= 1
#        else:
#            count +=1
#print(count+1)    


# 문제 번호 2908 상수
A,B = map(str, input().split()) #두 수 입력
A = int(A[::-1]) # 문자를 뒤집어서 출력
B = int(B[::-1])
print(max(A,B))


# 문제 번호 5622 다이얼
# 알파벳에 숫자를 먼저 할당해주고 걸리는 시간은 (숫자 +1)초임
# 문자만 입력하기 때문에 0과 1은 생각할 필요가  X
 
A = input()
alpha = " "
sum = 0
for a in A:
    if a == "A" or a == "B" or a == "C":
        alpha = "2"
    elif a == "D" or a == "E" or a == "F":
        alpha = "3"
    elif a == "G" or a == "H" or a == "I":
        alpha = "4"
    elif a == "J" or a == "K" or a == "L":
        alpha = "5"
    elif a == "M" or a == "N" or a == "O":
        alpha = "6"
    elif a == "P" or a == "Q" or a == "R" or a == "S":
        alpha = "7"
    elif a == "T" or a == "U" or a == "V":
        alpha = "8"        
    elif a == "W" or a == "X" or a == "Y" or a == "Z":
        alpha = "9"   
    
    sum += (int(alpha)+1)
    
print(sum)

# 찾아본 풀이
Number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
A = list(input())
time = 0 # 걸리는 시간 
for a in A:
    for n in Number:
        if a in n:
            time += Number.index(n) + 3 # index에 3초를 더해줘야 시간나옴
print(time)
            

# 문제 번호 2941 크로아티아 알파벳
#alpha = set(input())
alpha = input()
count = 0
Number = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

        
for n in Number:
    if n in alpha:
        count += alpha.count(n)   # 만약에 리스트 Number에 있는 단어들이 입력된 alpha에 있다면 그 개수를 카운트 해줌
print(len(alpha)-count) # 입력받은 alpha의 전체 길이에서 count를 빼주면 됨 


#for a in len(alpha):
#    if alpha[a] == "c":
#        if alpha[a + 1] == "="
#            count +=1
#        elif alpha[a + 1] == "-":
#            count +=1
#    elif alpha[a] == "d":
#        if alpha[a+1] == "z" and alpha[a+2] ==


# 문제 번호 1316 그룹 단어 체커
N = int(input()) # 반복횟수, 단어의 개수 

for i in range(N):
    word = input()
    for j in range(len(word)-1):  # 마지막 단어(j+1)까지 비교하기 위해 범위 len(word)-1
        if word[j] != word[j+1]:  # j와 j+1이 다른 경우만 비교 
             if word[j] in word[j+1:]:
                 N -= 1
                 break      
print(N)