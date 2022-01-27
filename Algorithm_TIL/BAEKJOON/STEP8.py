# 1712 손익분기점
# 손익분기점은 고정비용 + 가변비용 * n < 판매비용 * n
A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))
    
# 2292 벌집

n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup :
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)

# 10757 큰 수 A + B
A,B = map(int, input().split())
print(A+B)

# 1193 분수 찾기
n = int(input())
i = 0
while True:
	i += 1
	n -= i
	if n <= 0:
		n += i
		i += 1
		break
if i%2==0:
	print((i-n), '/', n, sep='')
else:
	print(n, '/', (i-n), sep='')
