import java.util.Scanner;

// 문제 : https://www.acmicpc.net/problem/1436 - 영화감독 숌
// 알고리즘 : 브루트 포스
public class ex_1436 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int count = 0;

        String num = "666"; // 666부터 시작 

        while (true) {
            if(num.contains("666")){ // 666이 숫자에 포함되어 있으면 count 증가
                count ++;
            }

            if(count == N){ // count가 N과 같다면 반복문 종료 (개수를 더이상 셀 필요가 없기 때문)
                break;
            }
            num = String.valueOf(Integer.parseInt(num) + 1); // num을 int로 바꿔준 후 +1을 해주고 666이 포함되어 있는지 판단하기 위해 String으로 재변환
        }

        System.out.println(num); // 반복문을 탈출하면 이때의 숫자 출력
    }
}
