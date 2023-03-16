import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class 보물_1026 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[] A = new int[N];
        ArrayList<Integer> B = new ArrayList<>();

        int sum = 0;

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        for (int i = 0; i < N; i++) {
            B.add(sc.nextInt());
        }

        Arrays.sort(A);

        int index = 0;
        int bIdx = 0;
        int max = B.get(0);

        while (!B.isEmpty()){
            max = B.get(0);
            for (int i = 0; i < B.size(); i++) {
                if(max <= B.get(i)){
                    max = B.get(i);
                    bIdx = i;
                }
            }

            sum += A[index] * max;
            B.remove(bIdx);
            index++;
        }

        System.out.println(sum);

    }
}
