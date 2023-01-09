package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

// 문제 : https://www.acmicpc.net/problem/2606 - 바이러스
// 알고리즘 : dfs
public class ex_2606 {
    public static int N,M,count ;
    public static ArrayList<Integer>[] graph;
    public static boolean[] visited;

    public static void dfs(int x){
        visited[x] = true;

        for (int i : graph[x]) {
            if(!visited[i]){
                count++;
                dfs(i);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        graph = new ArrayList[N+1];
        visited = new boolean[N+1];

        for (int i = 1; i < N+1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
             st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph[u].add(v);
            graph[v].add(u);
        }

        dfs(1);

        System.out.println(count);
    }

}
