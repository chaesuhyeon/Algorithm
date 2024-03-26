package src;

import java.util.*;

// 백준
public class ATM_11399 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int sum = 0;
        int tmp = 0;

        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            list.add(sc.nextInt());
        }
        Collections.sort(list);

        for (int i = 0; i <list.size(); i++) {
            tmp+= list.get(i);
            sum += tmp;
        }

        System.out.println(sum);
    }
}

