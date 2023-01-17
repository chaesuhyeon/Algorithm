import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

// 문제 : https://www.acmicpc.net/problem/7568 - 덩치
// 알고리즘 : 브루트포스 
public class ex_7568 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        List<int[]> list = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            int[] arr = new int[2]; // 몸무게와 키 
            arr[0] = sc.nextInt(); // 몸무게
            arr[1] = sc.nextInt(); // 키
            list.add(arr); // list에 데이터 추가
        }


        for (int i = 0; i < list.size(); i++) {
            int count = 1; // 마지막에 등수 + 1 안해주기 위해서 그냥 1부터 시작

            int[] num1 = list.get(i); // i번째의 몸무게와 덩치 배열 추출
            int x = num1[0];
            int y = num1[1];

            for (int j = 0; j < list.size(); j++) {
                if(i == j){ // i와 j가 같은 경우에는 비교하지 않도록 continue
                    continue;
                }
                int[] num2 = list.get(j); // j번째 (i가 아닌 데이터)의 몸무게와 키 배열 추출
                int a = num2[0];
                int b = num2[1];

                if(a > x && b > y){ // j번째의 데이터들이 더 크다면 count 증가
                    count ++;
                } else { // 몸무게와 키를 비교하여 등수를 매길 수 없는 경우 continue
                    continue;
                }
            }

            System.out.print(count + " "); // 출력

        }
    }
}
