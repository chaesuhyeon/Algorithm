# 1712 손익분기점
# 손익분기점은 고정비용 + 가변비용 * n < 판매비용 * n
A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))