package src;

import java.util.ArrayList;
import java.util.List;

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42839
// 알고리즘 : 브루트포스
public class 소수 {

    public static void main(String[] args) {
        System.out.println(new 소수().solution("17"));
    }

    public int solution(String numbers) {
        int answer = 0;
        List<String> list = new ArrayList<>();

        char[] charArr = numbers.toCharArray();
        for (int i = 0; i < charArr.length; i++) {

        }
        
        int num = 7;
        boolean flag = false;
        for (int i = 2; i < num/2; i++) {
            if(num % i == 0){
                flag = true;
            }
        }


        return answer;
    }
}
