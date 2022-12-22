import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

// 문제 : https://www.acmicpc.net/problem/4949 - 균형잡힌 세상
// 알고리즘 : 스택
public class ex_4949 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true){
            String[] s = sc.nextLine().split("");

            if(s[0].equals(".")){ // 마지막 입력 값이 .면 반복문 종료
                break;
            }
            
            Stack<String> st = new Stack<>();

            for (int i = 0; i < s.length; i++) {

                if(s[i].equals("(") || s[i].equals("[")){ // (거나 [면
                    st.push(s[i]); // 스택에 push
                } else if(s[i].equals(")")){ // ")" 라면 
                    if(!st.isEmpty() &&st.peek().equals("(")){ // 빈스택이 아니고, 마지막 원소가 (이면 pop 해준다
                        st.pop();
                    } else { // 그게 아니면 균형잡히지 않음
                        st.push(")");
                    }
                } else if(s[i].equals("]")){
                    if(!st.isEmpty() && st.peek().equals("[")){
                        st.pop();
                    } else {
                        st.push("]");
                    }
                }
            }
            if(st.isEmpty()){
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
        }
    }
}
