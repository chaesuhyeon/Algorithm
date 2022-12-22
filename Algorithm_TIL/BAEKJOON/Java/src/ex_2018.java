import java.util.Scanner;

// 문제 : https://www.acmicpc.net/problem/2018 - 수들의 합 5
// 알고리즘 : 투 포인터
public class ex_2018 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int cnt = 1;
        int start = 1;
        int end =1;
        int sum = 1;

        while (end != N){
            if(sum == N){ // 합이 N과 같으면
                cnt ++; // 개수 + 1
                end ++; // 조합 찾았으니까 end 포인트를 1개 이동 시킴
                sum += end; // sum에 end를 더해준다
            } else if (sum > N) { // sum이 N보다 크면 왼쪽을 삭제해줘야하기 때문에 start 빼주고 +1만큼 이동시킨다
                sum -= start;
                start ++;
            } else { // sum이 N 보다 작은경우
                end ++; // N보다 작은경우 end를 이동시켜서 연속된 조합을 찾는다
                sum += end; // end를 더해준다.
            }
        }
        System.out.println(cnt);
    }

}
