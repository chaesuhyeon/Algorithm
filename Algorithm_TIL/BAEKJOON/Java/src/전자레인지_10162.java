package src;

import java.util.Scanner;

public class 전자레인지_10162 {
    public static void main(String[] args) {
        int[] times = new int[]{300, 60, 10}; // 5분, 1분 , 10초
        int count = 0;

        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();


        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < times.length; i++) {
            count = T / times[i];
            T %= times[i];
            sb.append(String.valueOf(count)).append(" ");

        }

        if(T==0){
            System.out.println(sb.toString());
        } else {
            System.out.println(-1);
        }

    }

}
