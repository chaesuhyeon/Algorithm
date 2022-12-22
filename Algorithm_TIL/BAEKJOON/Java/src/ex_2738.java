import java.util.Arrays;
import java.util.Scanner;

// 문제 : https://www.acmicpc.net/problem/2738 - 행렬 덧셈
// 알고리즘 : 2차원 배열
public class ex_2738 {
        static Scanner sc = new Scanner(System.in);

        static int n = sc.nextInt();
        static int m = sc.nextInt();
    public static void main(String[] args) {

        int[][] arr1 = new int[n][m];
        int[][] arr2 = new int[n][m];

        make(arr1); // 행렬1 생성
        make(arr2); // 행렬2 생성

        // 행렬 합 구하기
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(arr1[i][j] + arr2[i][j]+" ");
            }
            System.out.println(); // 한 행의 합이 끝나면 줄바꿈
        }
    }

    // 행렬을 만드는 함수
    static void make(int[][] array){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                array[i][j] = sc.nextInt();
            }
        }
    }
}
