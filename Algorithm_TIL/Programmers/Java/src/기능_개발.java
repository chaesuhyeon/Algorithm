package src;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42586
// 알고리즘 : 스택
public class 기능_개발 {
    public static void main(String[] args) {
        new 기능_개발().solution(new int[]{93, 30, 55}, new int[]{1, 30, 5});
    }

    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        List<Integer> list = new ArrayList<>();

        Queue<Integer> q = new LinkedList<>();

        for(int i=0; i<progresses.length; i++){
            q.add((int) (Math.ceil((100.0 - progresses[i]) / speeds[i])));
        }


        while (!q.isEmpty()){
            int n = q.poll();
            int cnt = 1;

            while (!q.isEmpty() && n >=q.peek()){ // n이 더 클때까지 count 세줌
                cnt++;
                q.poll();
            }

            list.add(cnt);

        }

        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}
