public class 숨어있는_숫자의_덧셈_2 {
    public static void main(String[] args) {
        new 숨어있는_숫자의_덧셈_2().solution("aAb1B2cC34oOp");
    }

    public int solution(String my_string) {
        int answer = 0;
        String[] strArr = my_string.replaceAll("[a-zA-Z]"," ").split(" ");

        for(String s : strArr){
            if(!s.equals("")){
                answer += Integer.parseInt(s);
            }
        }

        return answer;
    }
}
