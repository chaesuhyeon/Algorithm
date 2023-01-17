import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

// 문제 : https://www.acmicpc.net/problem/1018 - 체스판 다시 칠하기
// 알고리즘 : 브루트포스
public class ex_1018 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        String[][] chess = new String[N][M];

        for (int i = 0; i < N; i++) {
            String str = sc.next();
            for (int j = 0; j < M; j++) {
                chess[i][j] = String.valueOf(str.charAt(j));
            }
        }

        char[] W = "WBWBWBWB".toCharArray();
        char[] B = "BWBWBWBW".toCharArray();
        int count = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {

            }
        }


    }
}
