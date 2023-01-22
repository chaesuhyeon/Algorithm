package src;// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/120871;

public class 저주의_숫자_3 {
    public static void main(String[] args) {
        new 저주의_숫자_3().solution(15);
    }

    public int solution(int n) {
        int answer = 0;

        for(int i=1; i<=n; i++){ // 문제에서 범위가 그렇게 크지 않으므로(최대 100) n만큼 반복문 돌림
            answer ++; // answer 하나씩 증가
            while(answer %3 ==0 || String.valueOf(answer).contains("3")){ // 증가된 answer가 3의 배수거나 3이 포함되어 있는 경우에는 계속 answer 하나씩 증가
                answer ++;
            }
        }
        return answer;
    }
}
