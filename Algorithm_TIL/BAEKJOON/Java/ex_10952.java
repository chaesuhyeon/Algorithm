import java.util.Scanner;

public class ex_10952 {
    public static void main(String[] args) {
        int A = 0;
        int B = 0;
        Scanner sc = new Scanner(System.in);

        do {
            A = sc.nextInt();
            B = sc.nextInt();
            if(A == 0 && B == 0){
                break;
            }
            System.out.println(A+B);
        } while (A != 0 && B != 0);
    }
}
