import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class ex_10610_30 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        String[] numbers = sc.next().split("");
        Arrays.sort(numbers, Comparator.reverseOrder());

        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            sum += Integer.parseInt(numbers[i]);
            sb.append(numbers[i]);
        }

        if(sum%3==0 && numbers[numbers.length-1].equals("0")){
            System.out.println(sb);
        } else {
            System.out.println(-1);
        }

    }
}

// 3의 배수 조건
// 각 자리수의 합이 3의 배수여야함

// 10의 배수 조건
// 2자리수 이상이면서, 자리수에 0이 있어야 10의 배수이다. -> 오름차순으로 정렬을 했을 때 맨 처음에 0이 와야 10의 배수이다.

// 30의 배수 조건
// 자리수 합이 3이면서 각 자리수를 오름차순으로 정렬을 했을 때 맨 처음에 0이 와야 30의 배수가 될 수 있다.
