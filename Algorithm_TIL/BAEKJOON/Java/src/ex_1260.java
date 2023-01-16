package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 문제 : https://www.acmicpc.net/problem/1260 - DFS와 BFS
// 알고리즘 : dfs, bfs
public class ex_1260 {
    public static int N,M,V;
    public static boolean[] visited;
    public static ArrayList<Integer>[] graph;

    public static void dfs(int x){
        visited[x] = true;

        System.out.print(x + " ");
        for (int i : graph[x]) {
            if(!visited[i]){
                dfs(i);
            }
        }
    }


    public static void bfs(int x){
        Queue<Integer> q = new LinkedList<>();
        visited[x] = true;
        q.offer(x);

        while (!q.isEmpty()){
            int y = q.poll();
            System.out.print(y + " ");
            for (int i : graph[y]) {
                if(!visited[i]){
                    q.offer(i);
                    visited[i] = true;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        visited = new boolean[N+1];

        for (int i = 1; i <=N ; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph[u].add(v);
            graph[v].add(u);
        }

        for (int i = 1; i < N+1; i++) {
            Collections.sort(graph[i]);
        }

        dfs(V);

        System.out.println();
        // 방문 배열 초기화
        visited = new boolean[N+1];
        bfs(V);
    }
}
