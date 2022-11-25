dict = {'zero' : 0 , 'one' : 1, 'two' : 2, 'three' : 3 , 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9 }

def solution(s):
    answer = ''
    alpha = ''
    for i in range(len(s)):
        if s[i].isdigit():
            answer += str(s[i])
        else:
            alpha += str(s[i])
            if alpha in dict:
                answer += str(dict[alpha])
                alpha=''
    return int(answer)

s = input()
print(solution(s))

# 다른 사람 풀이
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))
        print("s : ", s)

    return int(s)

s = input()
print(solution(s))