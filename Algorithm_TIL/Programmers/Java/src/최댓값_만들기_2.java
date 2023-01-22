package src;

import java.util.Arrays;

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/120862 
public class 최댓값_만들기_2 {
    public static void main(String[] args) {
        new 최댓값_만들기_2().solution(new int[]{1,2,-3,4,-5});
    }

    public int solution(int[] numbers) {
        int answer = 0;

        Arrays.sort(numbers);
        int num1= numbers[0] * numbers[1];
        int num2= numbers[numbers.length -1] * numbers[numbers.length -2];

        answer = Math.max(num1,num2);


        return answer;
    }
}
