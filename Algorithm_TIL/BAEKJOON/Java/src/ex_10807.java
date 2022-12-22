import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex_10807 {
    public static void main(String[] args) {
        List list = new ArrayList();
        List numList = new ArrayList();

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            numList.add(num);
        }

        int v = sc.nextInt();
        int cnt = 0;

        for (int i = 0; i < numList.size(); i++) {
            if((int)numList.get(i) == v){
                cnt ++;
            }
        }
        System.out.println(cnt);
    }
}
