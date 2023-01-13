import java.util.Scanner;

// 이코테
public class 이진_탐색_반복 {
    // 이진 탐색(반복)
    public static int binarySearch(int[] arr, int target, int start, int end){
        while (start <= end){

            // 중간 값 인덱스 구함
            int mid = (start + end) / 2;

            // 중간 값이 target과 같으면 인덱스 반환
            if(arr[mid] == target){
                return mid;
            } else if (arr[mid] > target){ // 중간 값보다 찾고자 하는 값이 작은 경우에는 중간 값보다 왼쪽 부분만 확인
                end = mid-1;
            } else {// 중간 값보다 찾고자 하는 값이 큰 경우에는 중간 값보다 왼쪽 부분만 확인
                start = mid +1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 원소의 개수(n)와 찾고자 하는 값(target)을 입력 받기
        int n = sc.nextInt();
        int target = sc.nextInt();

        // 전체 원소 입력 받기
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // 이진 탐색 수행 결과 출력
        int result = binarySearch(arr, target, 0, n-1);
        if(result== -1){
            System.out.println("원소가 존재하지 않습니다.");
        } else {
            System.out.println(result+1); // 인덱스(result) 이므로 몇 번째에 있는지(1부터 시작) 구하려면 인덱스 + 1 해줘야 함
        }
    }
}
