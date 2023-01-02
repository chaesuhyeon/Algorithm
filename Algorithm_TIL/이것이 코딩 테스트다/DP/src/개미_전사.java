import java.util.Scanner;

public class 개미_전사 {
    // 앞서 계싼된 결과를 저장하기 위한 DP 테이블 초기화
    public static int[] d = new int[100];
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int K = sc.nextInt();

        // 모든 식량 정보 입력 받기
        int[] arr = new int[K];
        for (int i = 0; i < K; i++) {
            arr[i] = sc.nextInt();
        }
        
        // 다이나믹 프로그래밍 진행 (보텀업)
        d[0] = arr[0];
        d[1] = Math.max(arr[0], arr[1]);

        for (int i = 2; i < K; i++) {
            d[i] = Math.max(d[i-1], d[i-2]+arr[i]);
        }

        // 계산된 결과 출력
        System.out.println(d[K-1]);
    }
}

// 입력예시
/*
4
1 3 1 5
*/

// 답
// 8
