import java.util.Scanner;

public class 이진_탐색_재귀 {
    public static int binarySearch(int[] arr, int target, int start, int end){
        if (start > end) return -1;

        int mid = start + end / 2; // 중간점 구하기
        if(arr[mid] == target){
            return mid;
        } else if(arr[mid] > target){
            return binarySearch(arr, target, start, mid-1);
        } else {
            return binarySearch(arr, target, mid+1, end);
        }

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 원소의 개수(n)와 찾고자 하는 값(target)을 입력받기
        int n = sc.nextInt();
        int target = sc.nextInt();

        // 전체 원소 입력받기
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // 이진 탐색 수행 결과 출력
        int result = binarySearch(arr, target, 0, n-1);
        if(result == -1){
            System.out.println("원소가 존재하지 않습니다");
        } else {
            System.out.println(result + 1);
        }
    }
}

/* 입력 예씨
10 7
1 3 5 7 9 11 13 15 17 19
 */

// 4 결과 값