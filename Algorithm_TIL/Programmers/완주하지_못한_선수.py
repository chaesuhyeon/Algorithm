# 예제는 통과했으나 시간초과 
def solution(participant, completion):
    answer = ''
    for i in range(len(completion)):
        if completion[i] in participant: # 완주자 명단에 있는 사람이 참여자 명단에 있다면 
            idx = participant.index(completion[i]) # 완주자를 참여자 명단에 몇번째에 있는지 인덱스를 찾아서 pop 해줌
            participant.pop(idx) # --> 인덱스 만큼의 시간복잡도 존재해서 시간초과 난듯 
    answer = participant[0] # 다 빼고나면 1명만 존재하기 때문에 대입해서 return 해줌 
          
    return answer

# 다시 풀이 - 성공 
# 삭제하려고하니까 시간초과 날 것 같아서 딕셔너리 이용 
def solution(participant, completion):
    answer = ''
    dic1 = {}
    dic2 = {}
    
    for i in participant:
        if i not in dic1: # 딕셔너리에 없는 데이터라면 1로 초기화 해줌
            dic1[i] =1
        else:             # 딕셔너리에 이미 존재하는 이름이라면 (동명이인) +=1 해줌 
            dic1[i] +=1
    
    for i in completion:
        if i not in dic2: # 딕셔너리에 없는 데이터라면 1로 초기화 해줌
            dic2[i] =1
        else:             # 딕셔너리에 이미 존재하는 이름이라면 (동명이인) +=1 해줌 
            dic2[i] +=1     
            
    
    for i in participant: # 참여자 명단에서 한명씩 뽑아서
        if (i not in dic2) or  dic1[i] != dic2[i]: # 완주자 명단에 없거나, dic1[참여자] = 값 과 dic2[완주자] = 값 이 다를 경우 이름은 중복인데, 참여자와 완주자의 수가 다르다고 판단 
            answer = i # 조건문을 만족하면 완주를 못한 사람이라는 뜻이므로 i를 answer에 대입 
        
    return answer # answer return 

# 다른 풀이 2- 성공
def solution(participant, completion):
    participant.sort() # 두 리스트 모두 정렬 
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]: # 앞부터 비교해서 만약에 다르면
            return participant[i] # 완주자가 없다는 뜻이므로 그 참가자를 바로 return 
    return participant[len(participant)-1] # 완주자 길이만큼 반복해줬는데도 return이 안끝나면 제일 마지막 참가자가 완주 못했다는 뜻