import java.util.Scanner;

public class 수들의_합_1789 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long N = sc.nextLong();

        long sum = 0;
        long num = 0;

        while (true){
            sum += num;
            if(sum > N){
                break;
            }
            num++;
        }

        System.out.println(num-1);
    }
}
