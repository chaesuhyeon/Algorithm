// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/120863
public class 다항식_더하기 {
    public static void main(String[] args) {
        new 다항식_더하기().solution("3x + 7 + x");

    }

    public static String solution(String polynomial) {
        String answer = "";
        String[] p = polynomial.split(" ");

        int sum1= 0;
        int sum2= 0;

        for(int i=0; i< p.length; i++){
            if(p[i].equals("+")) continue;
            if(p[i].contains("x")){
                if(p[i].length() != 1){
                    sum1 += Integer.parseInt(p[i].substring(0, p[i].length() - 1));
                } else {
                    sum1 += 1;
                }
            } else {
                sum2 += Integer.parseInt(p[i]);
            }
        }


        if(sum1 > 0){
            if(sum1 == 1){
                answer += "x";
            }
            else{
                answer += sum1 + "x";
            }
            if(sum2 > 0){
                answer += " + " + sum2;
            }
        }else{
            answer += String.valueOf(sum2);
        }
        return answer;
    }
}
