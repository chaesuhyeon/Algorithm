import java.util.Scanner;

// 문제 : https://www.acmicpc.net/problem/11047 - 동전 0
// 알고리즘 : 그리디
public class ex_11047 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] coin = new int[N];
        int cnt = 0;

        for (int i = 0; i < N; i++) {
            coin[i] = sc.nextInt();
        }

        for (int i = N-1; i>=0 ; i--) {
            if(coin[i] > K){
                continue;
            } else {
                cnt += (K / coin[i]);
                K = (K%coin[i]);
            }
        }

        System.out.println(cnt);

    }
}