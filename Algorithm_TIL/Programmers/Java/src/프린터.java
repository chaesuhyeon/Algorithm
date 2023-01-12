import java.util.LinkedList;
import java.util.Queue;

public class 프린터 {
    public static void main(String[] args) {
        new 프린터().solution(new int[]{2,1,3,2}, 2);
    }

    public static int solution(int[] priorities, int location) {
        // 초기화
        int answer = 0;
        Queue<int[]> que = new LinkedList<>();
        boolean flag = false;

        // que에 위치값, 우선순위 값 저장
        for(int i=0; i < priorities.length; i++){
            int num = priorities[i];
            que.offer(new int[]{i,num}); // i : 위치 값, num : 우선순위 값
        }

        while(!que.isEmpty()){
            int[] now = que.poll(); // que에서 하나 추출
            flag = true; // flag를 true로 우선 바꿔줌

            for (int[] q : que) { // 큐를 하나씩 돌면서
                if(q[1] > now[1]) { // 위에서 추출한 큐의 우선순위와 반복문에서 돌고있는 큐의 우선순위를 비교하여
                    flag = false; // now의 우선순위보다 큰 값이 있다면 flag를 false로 바꿔준다.
                    break;
                }
            }

            if(!flag){ // flag가 false가 나오면
                que.offer(now); // now를 큐 맨뒤에 다시 삽입한다.
            } else {
                answer++; // flag가 true이면 개수 + 1
                if(now[0] == location) break; // now의 위치값과 location과 같으면 while문 종료
            }

        }

        return answer;
    }
}
