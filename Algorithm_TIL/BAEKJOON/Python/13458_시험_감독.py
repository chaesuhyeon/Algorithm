import sys

room  = int(sys.stdin.readline().rstrip())
person = list(map(int,sys.stdin.readline().rstrip().split()))
b , c = map(int,sys.stdin.readline().rstrip().split())

cnt = 0

for i in range(room): # 시험장 개수만큼 반복
    if person[i] > 0 : # 시험장 하나당 있는 사람의 수가 0보다 크면 우선 총감독관이 감독하는 사람의 수 만큼 빼줌 (총감독관은 한명으로 제한) 
        person[i] -= b # 총 감독관 
        cnt += 1

    if person[i] > 0: # 부 감독관
        cnt += int(person[i]/c) # 부 감독관은 수 제한이 없으므로 필요한 부감독관의 수 만큼 count 
        if person[i] % c !=0: # 홀수인 경우 1명이 더 필요하므로 1명 더해줌
            cnt += 1

print(cnt) # 감독관 수 출력 