import java.util.ArrayList;
import java.util.List;

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42840
// 알고리즘 : 브루트포스
// 시간 초과
public class 모의고사 {
    public static void main(String[] args) {
        new 모의고사().solution(new int[]{1,2,3,4,5});
//        new 모의고사().solution(new int[]{1,3,2,4,2});
    }

    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();

        int[] one = new int[]{1,2,3,4,5};
        int[] two = new int[]{2,1,2,3,2,4,2,5};
        int[] three = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] cntArr = new int[3];
        int max ;

        for (int i = 0; i < answers.length; i++) {
            if(answers[i] == one[i% one.length]){ // anwer의 인덱스가 one을 초과할 경우 때문에 나머지로 나온 값을 인덱스로 사용하여 비교
                cntArr[0]++;
            }

            if(answers[i] == two[i% two.length]){
                cntArr[1]++;
            }

            if(answers[i] == three[i%three.length]){
                cntArr[2]++;
            }
        }

        max = Math.max(Math.max(cntArr[0],cntArr[1]), cntArr[2]); // max값 구하기

        for (int i = 0; i < cntArr.length; i++) {
            if(cntArr[i] == max){
                answer.add(i+1);
            }
        }



        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
