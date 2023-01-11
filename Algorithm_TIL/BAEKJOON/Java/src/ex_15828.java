import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

// 문제 : https://www.acmicpc.net/problem/15828 - Router
// 알고리즘 : 큐,덱
public class ex_15828 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        Queue<Integer> que = new LinkedList<>();

        while(true){
            int P = sc.nextInt();
            if(P == -1){
                break;
            }

            if(que.size() != N && P != 0){
                que.add(P);
            } else if (!que.isEmpty()&& P == 0){
                que.poll();
            }
        }

        if(que.size()==0){
            System.out.println("empty");
        } else {
            for (Integer i : que) {
                System.out.print(i + " ");
            }
        }
    }

}
