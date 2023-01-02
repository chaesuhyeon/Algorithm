import java.util.Scanner;

// 문제 : https://www.acmicpc.net/problem/1934 - 최소공배수
// 알고리즘 : 유클리드 호제법
// 최대 공약수 : 큰 수 % 작은 수 -> 앞 단계에서의 작은 수와 앞 단계에서의 결과값(나머지)의 연산을 수행 -> 나머지가 0이 되는 순간의 작은 수가 최대 공약수
// 최대 공배수 : A * B / 최대공약수
public class ex_1934 {
    public static int gcd(int x, int y){
        int m = x % y;
        if (m == 0){
            return y;
        }
        return gcd(y,m);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();

            if(A > B){
                System.out.println(A*B/gcd(A,B));
            } else {
                System.out.println(A*B/gcd(B,A));

            }
        }

    }
}
