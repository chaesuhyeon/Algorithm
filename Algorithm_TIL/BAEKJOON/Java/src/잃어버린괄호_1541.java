package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 잃어버린괄호_1541 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        int sum = 0;

        String[] minusArr = sc.nextLine().split("-");
        for (int i = 0; i < minusArr.length; i++) {
            if(minusArr[i].contains("+")){
                sum = 0;
                String[] plusArr = minusArr[i].split("[+]");
                for (int j = 0; j < plusArr.length; j++) {
                    sum += Integer.parseInt(plusArr[j]);
                }
                list.add(sum);
            } else {
                list.add(Integer.parseInt(minusArr[i]));
            }

        }
        int result = list.get(0);
        for (int i = 1; i <list.size(); i++) {
            result -= list.get(i);
        }

        System.out.println(result);
    }
}