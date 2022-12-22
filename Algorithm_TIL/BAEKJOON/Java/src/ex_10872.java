import java.util.Scanner;

public class ex_10872 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();

        int result = facto(num);
        System.out.println(result);

    }

    public static int facto(int num){
        if(num<=1){
            return 1;
        } else {
            return num * facto(num-1);
        }
    }
}
