import java.util.Scanner;
import java.util.Stack;

public class ex_9012 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack st = new Stack();
        int T = sc.nextInt(); // 테스트 케이스 입력 받기

        for (int i = 0; i < T; i++) {
            String parse = sc.next(); // nextLine 안됨!!

            for (int j = 0; j < parse.length(); j++) {
                char ch = parse.charAt(j); // 문자열을 문자로 바꿔줌

                if (ch == '('){
                    st.push(ch); // '( '이면 스택에 push
                } else { // ')'인 경우
                    if(!st.isEmpty()){ // 스택이 빈스택이 아닐 경우에만
                        st.pop(); // 마지막에 추가된 '(' pop
                    } else { // ')' 인데, 스택이 비었다면
                        st.push(ch); // ')'를 스택에 추가 (이미 짝이 안맞음)
                        break;
                    }
                }

            }
            if(st.isEmpty()){ // 스택이 비었다면 알맞게 pop아 됐으므로 올바른 괄호
                System.out.println("YES");
            } else { // 스택이 비지 않았다면 짝이 안맞는 괄호
                System.out.println("NO");
            }
            st.clear(); // 1개의 반복문이 끝나면 스택을 꼭 초기화 시켜줘야 함!!
        }
    }
}
