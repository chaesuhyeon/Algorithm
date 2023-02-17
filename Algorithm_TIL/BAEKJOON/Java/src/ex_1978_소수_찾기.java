package src;

import java.util.Scanner;

public class ex_1978_소수_찾기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int p = 0;
        int cnt =0;

        for (int i = 0; i < n; i++) {
            p = sc.nextInt(); // 입력을 받은 수를 p에 저장
            if(isPrime(p) == true){ // 소수라고 판별이 되면
                cnt +=1; // 카운트 증가
            }
        }
        System.out.println(cnt); // 카운트 출력
    }

    public static boolean isPrime(int n) {

        if(n == 1){ // 1은 소수가 아니기 때문에 제외 시켜줌
            return  false;
        }

        for (int i = 2; i<= Math.sqrt(n); i++) { // 범위는 2부터 n의 제곱근까지
            if (n % i == 0) { // n을 i로 나눴을때 0이 된다면 소수가 아님(나눠지는 숫자가 존재하는 순간 소수가 아님)
                return false;
            }
        }
        return true; // 반복문을 검사해서 n을 i로 나눠줬는데 나머지가 0이 되지 않는다면 소수이므로 true로 return 해준다
    }
}
