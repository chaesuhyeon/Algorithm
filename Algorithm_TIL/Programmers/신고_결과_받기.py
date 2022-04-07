def solution(id_list, report, k):
    answer = []
    result = [0] * len(id_list)
    dic = {}
    
    for i in id_list:
        dic[i] = 0 # 먼저 딕셔너리에 사람 넣고 0으로 초기화

    s_report = set(report)    

    for i in s_report:
        x, y = i.split() # 공백간격으로 report 잘라서 answer에 이중리스트로 넣어주기 [[muzi, frodo], [apeach, frodo]]
        answer.append([x,y])
        
         
    for i in answer: # 신고당한 유저 +1 해주기 
        a = i[1] 
        dic[a] += 1

    for i in range(len(answer)): # for문 돌려가며 신고당한 유저값을 키로 갖는 딕셔너리에서 value값을 찾아서 횟수가 k번 이상이면 
        re = answer[i][1]
        if dic[re] >= k:
            idx = id_list.index(answer[i][0]) # 신고한 유저의 인덱스를 찾아서
            result[idx] += 1 # result에 그 인덱스에 맞는 값을 +1해줌 
          
    return result