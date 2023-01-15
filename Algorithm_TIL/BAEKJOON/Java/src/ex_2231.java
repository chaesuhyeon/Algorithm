import java.util.Scanner;

// 문제 : https://www.acmicpc.net/problem/2231 - 분해합
// 알고리즘 : 브루트포스
public class ex_2231 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String N = sc.nextLine();

        String num = N; // 값을 변동해야하고 최솟값을 찾아야하므로 N부터 시작(1씩 줄여나가서 분해합의 최솟값을 찾기)
        int min = 0;

        while (Integer.parseInt(num) !=0){ // num이 0이면 반복문 종료
            int sum = 0;

            for (int i = 0; i < num.length(); i++) {
                sum += num.charAt(i) - '0'; // 한자리씩 sum에 더함
            }
            sum += Integer.parseInt(num); // num을 sum에 더함 ex) 216 = 198 + 1 + 9 + 8; 

            if(sum == Integer.parseInt(N)){ // 합계가 N과 같다면
                min = Integer.parseInt(num); // num을 저장 
                num = String.valueOf(Integer.parseInt(num) -1); // 분해합의 최솟값을 구해야하기 때문에 num을 1씩 줄여가며 분해합의 최솟값 찾기
            } else {
                num = String.valueOf(Integer.parseInt(num) -1); // 합계가 N과 다르다면 그냥 num만 -1 해주기 (min값 저장x)
            }
        }

        System.out.println(min); // min값 출력
    }
}
