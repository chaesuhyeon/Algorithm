# 11047 동전0
n, k = map(int, input().split())
arr = [None] * n

cnt = 0 

for i in range(n):
    arr[i] = int(input()) # 동전들 하나씩 입력받음


for i in range(n-1, -1, -1): # 큰 화폐 단위부터 체크 
    if arr[i] > k: # 만들어야하는 단위인 k보다 화폐단위가 큰 동전이라면 무시하고 다시 반복분 실행
        continue
    else: # k가 더 크다면
        cnt += k//arr[i] # k로 최대한 만들 수 있는 만큼 만들어야 하기 때문에 몫을 cnt에 더해줌  
        k %= arr[i] # k로 만들고 난 후의 나머지를 구함 
print(cnt) # 횟수 출력 


# 1931 회의실 배정
n = int(input())
meet= []

for _ in range(n):
    start, end = map(int, input().split()) # 회의 시작시간과 끝나는 시간을 입력받고
    meet.append([start, end]) # 회의 리스트에 추가

meet.sort(key=lambda x: (x[1], x[0]) ) # 회의 끝나는 시간을 기준으로 정렬하고, 회의 끝나는 시간이 같다면 시작하는 순서대로 정렬
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

cnt = 1 # 첫번째 회의개수부터 시작 
start = meet[0][0] # 정렬한것 첫번째 시작시간 [1]
end = meet[0][1] # 정렬한것 첫번째 끝나는 시간 [4]


for i in range(1,n): # 두번째 회의부터
    if meet[i][0] >= end:  #  그 전 회의 end 시간보다 두번째 회의 start가 더 크면 
        start = meet[i][0] # start를 그 다음 회의 start로 바꿔줌
        end = meet[i][1] # end를 그 다음 회의 end로 바꿔줌
        cnt += 1 # cnt 늘려주기 
    else: # 그 전 회의 end 시간보다 두번째 회의 start가 작으면 회의 시작을 하지 못하므로 
        continue # 무시함 

print(cnt) 

# 13305 주유소
# 처음풀이 17점.. 너무 단순하게 생각함,, (이전 지역의 가격만 고려) --> 최소 가격이 나오면 그 가격으로 주유해서 쭉 가는게 나은데.., 고려 안했음

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = distance[0] * price[0] # 첫 시작 

for i in range(1, len(distance)): # 두번째 원소부터 비교
    if price[i-1] >= price[i]: # 전 지역의 가격이 더 클경우
        result += (price[i] * distance[i]) # 그냥 위아래 곱함
    else: # 전 지역의 가격이 저렴할 경우
        result += (price[i-1] * distance[i]) # 현재 거리 수 * 전 지역의 주유소 가격

print(result)


# 다른 풀이
n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
min_price = price[0] # 첫번째 값으로 초기화 (무조건 처음 가격으로 주유를 해야하므로)
for i in range(n-1):
    if price[i] < min_price: # 가격이 더 작은 주유소가 나오면 그 주유소 가격으로 바꿔줌
        min_price = price[i]
    result += (min_price * distance[i])
print(result)