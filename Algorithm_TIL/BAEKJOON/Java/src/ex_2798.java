import java.util.Arrays;
import java.util.Scanner;

// 문제 : https://www.acmicpc.net/problem/2798 - 블랙잭
// 알고리즘 : 브루트포스
public class ex_2798 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N  = sc.nextInt();
        int M = sc.nextInt();
        int[] arr = new int[N];
        int max = 0;

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr); // 정렬해서 하나씩 비교함!

        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                for (int k = j+1; k < N; k++) {
                    int tmp = arr[i] + arr[j] + arr[k];
                    if(tmp > max && tmp <= M){
                        max = tmp;
                    }
                }
            }
        }

        System.out.println(max);
    }
}
