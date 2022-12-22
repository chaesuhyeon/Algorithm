import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 문제 : https://www.acmicpc.net/problem/18258
// 알고리즘 : 큐
public class ex_18258 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        Deque<String> que = new LinkedList<>();

        StringBuilder sb = new StringBuilder();
        StringTokenizer st ;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            switch (st.nextToken()){
                case "push":
                    que.add(st.nextToken());
                    break;
                case "front":
                    if(que.isEmpty()){
                        sb.append("-1\n");
                        break;
                    } else {
                        sb.append(que.peekFirst()+"\n");
                        break;
                    }
                case "back":
                    if(que.isEmpty()){
                        sb.append("-1\n");
                        break;
                    } else {
                        sb.append(que.peekLast()+"\n");
                        break;
                    }
                case "pop":
                    if(que.isEmpty()){
                        sb.append("-1\n");
                        break;
                    } else {
                        sb.append(que.pollFirst()+"\n");
                        break;
                    }
                case "size":
                    sb.append(que.size()+"\n");
                    break;
                case "empty":
                    sb.append(que.isEmpty()? 1+"\n" : 0 +"\n");
            }
        }
        System.out.println(sb.toString());
    }
}
