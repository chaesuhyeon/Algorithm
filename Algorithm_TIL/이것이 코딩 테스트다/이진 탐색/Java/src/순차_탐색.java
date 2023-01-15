import java.util.Scanner;

public class 순차_탐색 {
    
    // 순차 탐색 소스 코드
    public static int sequantialSearch(int n, String target, String[] arr){
        
        // 각 원소를 하나씩 확인하며
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
            
            // 현재의 원소가 찾고자 하는 원소와 동일한 경우
            if(arr[i].equals(target)){
                return i+1; // 현재위 위치 반환(인덱스는 0부터 시작하므로 1 더하기)
            }
        }
        
        return -1; // 원소를 찾지 못한 경우 -1 반환
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // 원소의 개수
        int n = sc.nextInt();
        // 찾고자 하는 문자열
        String target = sc.next();

        String[] arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.next();
        }

        // 순차 탐색 수행 결과 출력
        System.out.println(sequantialSearch(n, target, arr));
     }
}

