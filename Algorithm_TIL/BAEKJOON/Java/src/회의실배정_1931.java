package src;

import java.util.*;

public class 회의실배정_1931 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        List<int[]> list = new ArrayList<>();
        int[] arr;
        int count = 1;

        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            arr = new int[]{x,y};
            list.add(arr);
        }

        // 끝나는 시간을 기준으로 정렬하기 위해 compare 재정의
        Collections.sort(list, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {

                // 종료시간이 같을 경우 시작시간이 빠른순으로 정렬해야한다.
                if(o1[1] == o2[1]) {
                    return o1[0] - o2[0];
                }
                return o1[1] - o2[1];
            }
        });

        int end = list.get(0)[1];

        for (int i = 1; i < N; i++) {
            if(list.get(i)[0] >= end){
                end = list.get(i)[1];
                count ++;
            }
        }

        System.out.println(count);

    }
}
