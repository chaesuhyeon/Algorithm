package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

// 문제 : https://www.acmicpc.net/problem/24479 - 알고리즘 수업 - 깊이 우선 탐색 1
// 알고리즘 : dfs
public class ex_24479 {

    public static int N,M,R,cnt;
    public static boolean[] visited;
    public static int[] answer;
    public static ArrayList<Integer>[] graph;

    public static void dfs(int x){
        visited[x] = true;
        answer[x] = ++cnt; // 순서 배열(방문하지 않은 배열은 자동으로 0)

        for (int i : graph[x]) {
            if(!visited[i]){
                dfs(i);
            }
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        visited = new boolean[N+1];
        graph = new ArrayList[N+1];
        answer = new int[N+1];

        for (int i = 1; i < N+1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 1; i < M+1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph[u].add(v);
            graph[v].add(u);
        }

        for (int i = 1; i < N+1; i++) {
            Collections.sort(graph[i]);
        }
        visited[R] = true;
        dfs(R);

        for (int i = 1; i < answer.length; i++) {
            sb.append(answer[i]).append("\n");
        }

        System.out.println(sb);
    }
}
