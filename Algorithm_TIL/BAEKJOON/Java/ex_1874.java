import java.io.*;
import java.util.*;

// 문제 : https://www.acmicpc.net/problem/1874
// 알고리즘 : 스택
public class ex_1874 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        Stack<Integer> st = new Stack<>();

        int count = 1;
        boolean b = true;

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            while (count <=num){
                st.push(count);
                sb.append("+\n");
                count++;
            }
            int last = st.peek();
            if (last == num){
                st.pop();
                sb.append("-\n");
            } else {
                b = false;
            }
        }

        if(b == false){
            System.out.println("NO");
        } else {
            System.out.println(sb.toString());
        }
    }
}
