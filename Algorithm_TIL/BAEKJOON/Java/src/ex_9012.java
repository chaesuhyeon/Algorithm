import java.util.Scanner;
import java.util.Stack;

// 문제 : https://www.acmicpc.net/problem/9012 - 괄호
// 알고리즘 : 스택
public class ex_9012 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < T; i++) {
            Stack<String> st = new Stack<>();
            String[] sArr = sc.nextLine().split("");
            for (int j = 0; j < sArr.length; j++) {
                if(sArr[j].equals("(")){
                    st.push(sArr[j]);
                } else if(sArr[j].equals(")") && st.size()==0){ // )일경우 size가 0이 아닐 때 (가 존재하지 않으므로 push해서 잘못된 괄호임을 파악
                    st.push(sArr[j]);
                } else if(sArr[j].equals(")") && !st.peek().equals(")")){ // 스택에 값이 존재하는데 )가 아닌 경우에만 pop해서 (를 제거
                    st.pop();
                }
            }

            if (st.size() ==0){
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
