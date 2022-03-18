# 통과
new_id = input()
def solution(new_id):
    answer = []
    string = ''
    id = new_id.lower()
    for i in range(len(id)):
        print("id[i] :", id[i])
        if id[i].isalpha() or id[i].isdigit() or id[i] == "-" or id[i] == "_" or id[i] == ".":
            if id[i] == ".":
                if answer:
                    if answer[-1] == ".":
                        continue
                    else:
                        answer.append(id[i])
            else:
                answer.append(id[i])
    if answer:            
        if answer[0] == ".":
            answer.pop(0)
        if answer[-1] == ".":
            answer.pop()

    if len(answer) == 0:
        answer.append("a")

    if len(answer) >= 16:
        answer = answer[:15]
        print("anwser 16 : ", answer)
        if answer[0] == ".":
            answer.pop(0)
        if answer[-1] == ".":
            answer.pop()

    last = answer[-1]             
    while len(answer) < 3:
        if len(answer) <= 2:
            answer.append(last)

 
    for i in answer:
        string += i
    
    return string

print(solution(new_id))


# 다른 사람 풀이중에 배울 코드
while '..' in answer:
    answer = answer.replace('..', '.')
