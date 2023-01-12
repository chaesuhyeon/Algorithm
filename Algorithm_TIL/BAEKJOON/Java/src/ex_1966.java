import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

// 문제 : https://www.acmicpc.net/problem/1966 - 프린터 큐
// 알고리즘 : 큐
public class ex_1966 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<int[]> que ;

        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {

            // 테스트 케이스마다 초기화
            int N = sc.nextInt();
            int M = sc.nextInt();
            int max = 9; // 문제에서 최대 중요도 값은 9라고 나옴
            int count = 0; // 몇 번째로 빠졌는지 체크하기 위해 선언
            int[] answer = new int[10]; // 문제에서 중요도가 1~9라고 했으므로 인덱스 그대로 쓰기 위해 9+1 = 10으로 길이 설정
            que  = new LinkedList<>();

            // 증요도와 위치값 int 배열로 que에 저장
            for (int j = 0; j < N; j++) {
                int p = sc.nextInt();
                que.add(new int[]{j,p}); // j : 위치값(0부터 시작), p : 중요도
                answer[p]++; // 중요도 개수를 저장
            }

            while (!que.isEmpty()){
                while (!que.isEmpty() && answer[max] == 0){ // que size가 0이 아니고, 중요도의 개수가 0이 되면 max값을 -1 해줌
                    max--;
                }
                int[] q = que.poll(); // que에서 배열 한개씩 poll
                if(q[1] != max){ // 뽑은 que의 중요도가 max가 아니면 맨 뒤에 삽입
                    que.offer(q);
                } else {
                    if(q[0] == M){ // 뽑은 que의 중요도가 max와 같고 위치가 M과 같다면
                        count ++; // count +1 해주고 count 출력
                        System.out.println(count);
                        break; // while문 종료
                    } else {
                        count ++; // 뽑은 que의 중요도가 max와 같지만 위치가 M이 아니라면 count 증가
                        answer[max]--; // 중요도 개수 1개 빼줌
                    }
                }
            }
        }

    }
}
