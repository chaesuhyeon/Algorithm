import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

//문제: https://www.acmicpc.net/problem/2164 - 카드2
// 알고리즘 : 큐, 덱
public class ex_2164 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());

        Deque<Integer> d = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            d.add(i+1);
        }

        while (d.size() > 1 ){
            d.pollFirst();
            d.add(d.pollFirst());
        }

        System.out.println(d.peek());
    }
}
