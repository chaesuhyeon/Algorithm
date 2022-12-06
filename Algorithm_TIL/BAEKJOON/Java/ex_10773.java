import java.util.Scanner;
import java.util.Stack;

// 문제 : https://www.acmicpc.net/problem/10773 - 제로
// 알고리즘 : 스택
public class ex_10773 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int K = Integer.parseInt(sc.nextLine());

        Stack<Integer> st = new Stack<>();

        for (int i = 0; i < K; i++) {
            int num = Integer.parseInt(sc.nextLine());

            if(num ==0 && st.size()>0){
                st.pop();
            } else {
                st.push(num);
            }
        }

        int sum = 0;
        for (Integer s : st) {
            sum +=s;
        }

        System.out.println(sum);
    }
}
