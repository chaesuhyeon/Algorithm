package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

// 이 문제는 A -> B로 계산하면서 푸는것이 아니라 B->A로 계산해가면서 풀어야한다.
public class AtoB_16953 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        int count = 1;
        while (B != A) {
            if( B < A ) { // B가 A보다 작으면 A로 B를 만들 수 없음
                System.out.println(-1); // 바로 -1 출력하고 종료
                return;
            }
            String str = String.valueOf(B); // 추후 B에서 1을 제거해주기 위해 str 선언
            if(B % 2 == 0) { // 2로 나눠지면
                B /= 2; // B를 2로 나눔
            } else if(str.charAt(str.length() - 1) == '1') { // B의 마지막 글자가 1이면 1을 제거해준다.
                str = str.substring(0, str.length() - 1); // 1 제거
                B = Integer.parseInt(str); // B를 1제거한 숫자로 다시 만들어줌 (ex. 42001 -> 4200)
            } else { //2로도 안나눠지고 끝 숫자가 1도 아니면 만들 수 없음 (연산이 2를 곱하거나 1을 끝에 추가해주거나 두개밖에 없으므로)
                System.out.println(-1); // -1 출력하고 종료함
                return;
            }
            count++; // 종료가 안되면 count 증가
        }

        System.out.println(count); // count 출력
    }
}
