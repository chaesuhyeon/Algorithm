import java.util.Stack;

public class Valid_Parentheses {
    public static boolean isValid(String s) {
        char[] charArr = s.toCharArray();

        Stack<Character> stack = new Stack<>();

        if (charArr.length == 1) {
            return false;
        }

        for (int i = 0; i < charArr.length; i++) {
           if(charArr[i] == '(' || charArr[i] == '{' || charArr[i] == '[') {
               stack.push(charArr[i]);
           } else if (charArr[i] == ')' || charArr[i] == '}' || charArr[i] == ']') {

               if (stack.isEmpty()) {
                   return false;
               }

               switch (charArr[i]) {
                   case ')' :
                       if (stack.pop() == '(') {
                           stack.pop();
                       } else {
                           return false;
                       }
                       break;
                   case '}':
                       if (stack.peek() == '{') {
                           stack.pop();
                       } else {
                           return false;
                       }
                       break;

                   case ']':
                       if (stack.peek() == '[') {
                           stack.pop();
                       } else {
                           return false;
                       }
                       break;
               }
           }
        }

        if (!stack.isEmpty()) {
            return false;
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(isValid("()"));
        System.out.println(isValid("()[]{}"));
        System.out.println(isValid("(]"));
        System.out.println(isValid("{[]}"));
        System.out.println(isValid("(("));
        System.out.println(isValid("){"));
        System.out.println(isValid("(){}}{"));
        System.out.println(isValid(")(){}"));
    }
}
