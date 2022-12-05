# 내 풀이  --> dic이용해서 a ~ h에 숫자 부여 (ex) a : 1 / ... / h : 8 
#  location = input()
# direction = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]


# cnt = 0
# for i in range(len(direction)):


# 책 풀이
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        result += 1

print(result)