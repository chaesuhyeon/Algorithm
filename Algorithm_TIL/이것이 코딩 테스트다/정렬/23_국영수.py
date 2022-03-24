# 메모리 60852
import sys
n = int(sys.stdin.readline().rstrip())

arr = [0] * n
for i in range(n):
    name, kor, eng, math = map(str, sys.stdin.readline().rstrip().split())

    arr[i] = (name, int(kor), int(eng), int(math))

arr.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in arr:
    print(i[0])
