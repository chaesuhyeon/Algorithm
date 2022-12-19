import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.StringJoiner;

// 문제 : https://www.acmicpc.net/problem/11866 - 요세푸스 문제 0
// 알고리즘 : 큐,덱
public class ex_11866 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        List<String> list = new ArrayList<>();

        for (int i = 1; i <=N ; i++) {
            list.add(String.valueOf(i)); // 1 ~ N 만큼 String으로 리스트에 넣어줌
        }

        StringJoiner sj = new StringJoiner(", ", "<", ">"); // 출력 형식 맞추기 위해 선언

        int index=0;

        for (int i = 0; i < N; i++) {
            index += K-1; // 인덱스는 K에서 1씩 작음
            
            if(index >= list.size()){ // 인덱스가 리스트 크기보다 같거나 크면
                index %= list.size(); // 리스트 사이즈로 인덱스를 나눠준다
            }
            sj.add(list.remove(index)); // 인덱스 위치에 있는 숫자를 제거
        }

        System.out.println(sj.toString()); // < , , , > 형식으로 출력

    }
}