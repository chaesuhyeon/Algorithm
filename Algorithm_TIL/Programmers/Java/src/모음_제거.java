package src;

public class 모음_제거 {
    public static void main(String[] args) {
        new 모음_제거().solution("nice to meet you");
    }

    public String solution(String my_string) {
        String answer = "";
        answer = my_string.replaceAll("[aeiou]","");
        return answer;
    }
}
