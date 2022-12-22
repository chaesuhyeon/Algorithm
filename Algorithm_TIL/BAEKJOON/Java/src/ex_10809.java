import java.util.Scanner;

// 문제 : https://www.acmicpc.net/problem/10809 - 알파벳 찾기
// 알고리즘 : 문자열
public class ex_10809 {
    public static void main(String[] args) {
        String[] s = "abcdefghijklmnopqrstuvwxyz".split("");

        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();

        for(int i=0; i<s.length; i++){
            if(word.contains(s[i])){
                System.out.print(word.indexOf(s[i]) + " ");
            } else {
                System.out.print(-1 + " ");
            }
        }
    }
}
