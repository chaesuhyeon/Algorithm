import java.util.Stack;

public class 올바른_괄호 {
    public static void main(String[] args) {
        new 올바른_괄호().solution("()()");
    }

    boolean solution(String s) {
        boolean answer = true;

        Stack<Character> st = new Stack<>();
        for(int i=0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c== '('){
                st.push('(');
            } else if(st.isEmpty() && c==')'){
                st.push(')');
            } else if(!st.isEmpty() && c==')'){
                st.pop();
            }

        }
        if(st.isEmpty()){
            answer = true;
        } else {
            answer = false;
        }

        return answer;
    }
}
