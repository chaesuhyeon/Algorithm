import sys

n = int(sys.stdin.readline().rstrip()) # 사람 수 
p = list(map(int,sys.stdin.readline().rstrip().split())) # 각 사람이 돈을 인출하는데 걸리는 시간 p
result = 0 # 최종 결과 값
tmp = 0 # 중간 저장 값 

p.sort() # 먼저 오름차순으로 정렬 

for i in p : # 시간을 하나씩 꺼내서 
    tmp += int(i) # 누적 중간 값 구해줌

    result += tmp # 누적된 중간 값을 최종 값에 누적으로 더해줌 

print(result)