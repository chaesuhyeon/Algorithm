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
#


# 문제 번호 1157 단어 공부
#



