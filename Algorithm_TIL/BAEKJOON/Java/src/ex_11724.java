package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

// 문제 :
// 알고리즘 : dfs
public class ex_11724 {
    public static int n,m;
    public static ArrayList<Integer>[] graph;
    public static boolean[] visited;
    public static void dfs(int x){
        if (visited[x]) return;

        // x를 방문하지 않다면 방문 처리
        visited[x] = true;

        // x의 깊이에 해당하는 노드들을 검사 -> 방문하지 않았을 경우 dfs 수행해서 방문 처리
        for (int i : graph[x]) {
            if(!visited[i]){
                dfs(i);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st  = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());


        // 숫자가 1부터 시작하므로 인덱스 편하게 쓰기 위해서 0은 사용하지 않고 1~n의 숫자 사용
        visited = new boolean[n+1];
        graph = new ArrayList[n+1];

        // 초기화
        for(int i=1; i< n+1; i++){
            graph[i] = new ArrayList<>();
        }

        // 입력 받기
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            // 방향이 없는 그래프이므로 양쪽 다 입력
            graph[u].add(v);
            graph[v].add(u);
        }

        int count = 0;
        for (int i = 1; i < n+1; i++) {
            // 방문하지 않은 노드일 경우에만 dfs 수행
            if(!visited[i]) {
                count++;
                dfs(i);
            };
        }

        System.out.println(count);
    }
}
// 이미 한번 돌 때 깊이에 있는 노드들을 다 방문하기 때문에 끊긴 경우에만 새롭게 방문하게됨(false)인 상태
