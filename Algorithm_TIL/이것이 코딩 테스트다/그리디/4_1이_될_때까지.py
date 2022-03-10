N, K = map(int,input().split())
cnt = 0

while True :
    if N % K == 0: # N이 K로 나누어 떨어지면
        N /= K # N을 K로 나눔 
        cnt += 1 # count + 1

        if N == 1: # 나눴는데 N이 1이되면 반복문 종료
            break

    else:
        N -= 1 # N이 K로 나누어 떨어지지 않으면 1 빼줌
        cnt += 1 # count += 1
        if N == 1: # 뺐는데 N이 1이되면 반복문 종료
            break

print(cnt) # 횟수 출력 