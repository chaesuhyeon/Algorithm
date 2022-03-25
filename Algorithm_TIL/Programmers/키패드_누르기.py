# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# hand = "right"

def solution(numbers, hand):
    answer = ''
    dic = {1:"L", 4:"L", 7:"L", 3:"R", 6: "R", 9:"R"}
    left = 10 # "*" 거리 계산을 위해 바꿔줌
    right = 12 # "#" 거리 계산을 위해 바꿔줌
    for number in numbers:
        if number in dic:
            answer += dic[number]
            if dic[number] == "L":
                left = number

            else:
                right = number
        else:
            if number == 0 : # 거리 계산을 위해 바꿔줌
                number = 11
            # 거리 구하는 법 
            # (두 넘버패드의 거리 차이의 절대값) / 3 의 몫 + 나머지
            # (|목표 키패드 - 현재 손 위치| % 3) + (|목표 키패드 - 현재 손 위치|//3)
            abs_left = abs(number- left)
            abs_left_sum = (abs_left // 3) + (abs_left%3)
            abs_right = abs(number - right)
            abs_right_sum = (abs_right // 3) + (abs_right%3)

            if abs_left_sum < abs_right_sum:
                answer += "L"
                left = number

            elif abs_left_sum > abs_right_sum:
                answer += "R"
                right = number

            # else: # 길이(거리)가 같을 때
            elif abs_left_sum == abs_right_sum:
                if hand == "left":
                    answer += "L"
                    left = number

                else:
                    answer += "R"
                    right = number

    return answer

print(solution(numbers, hand))