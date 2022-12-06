import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

public class ex_10828 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());

        Stack<String> st = new Stack<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            String[] s = sc.nextLine().split(" ");

            if(s[0].equals("push")){
                st.push(s[1]);

            } else if (s[0].equals("top")){
                if(st.size()>0){
                    sb.append(st.peek()+"\n");
                } else {
                    sb.append("-1" +"\n");

                }

            } else if(s[0].equals("empty")){
                if(st.size()==0){
                    sb.append("1" +"\n");
                } else {
                    sb.append("0" +"\n");
                }
            } else if(s[0].equals("size")){
                sb.append(st.size()+"\n");
            } else { //pop
                if(st.size()>0){
                    sb.append(st.pop()+"\n");
                } else {
                    sb.append("-1"+"\n");
                }
            }
        }
        System.out.println(sb.toString());
    }
}
