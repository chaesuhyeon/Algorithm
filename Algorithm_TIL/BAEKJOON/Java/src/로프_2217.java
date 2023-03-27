import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 로프_2217 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        Integer[] rope = new Integer[N];

        for (int i = 0; i < N; i++) {
            rope[i] = sc.nextInt();
        }
        Arrays.sort(rope , Collections.reverseOrder());;

        int mw =0; // max weight

        for (int i = 0; i < N; i++) {
            mw = Math.max(mw, rope[i] * (i + 1)); // 큰값부터 비교해서, 큰 값 x 1 과 작은 값 x 로프의 개수를 비교해서 더 큰값이
        }

        System.out.println(mw);

    }
}