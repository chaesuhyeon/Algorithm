package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 문제 : https://www.acmicpc.net/problem/24444 - 알고리즘 수업 - 너비 우선 탐색 1
// 알고리즘 : bfs
public class ex_24444 {
    static int N,M,R,Idx;
    static int[] answer;
    static boolean[] visited;
    static ArrayList<Integer>[] A;
    public static void BFS(int x){
        Queue<Integer> q = new LinkedList<>();
        q.offer(x); // 첫 노드를 큐에 저장
        visited[x] = true; // 방문 처리

        while (!q.isEmpty()){ // 큐가 빌 때 까지 반복
            int y = q.poll();
            answer[y] = ++Idx; // 순서배열에 순서를 저장
            for (int i : A[y]) { // y에 연결된 노드들을 돌면서 방문하지 않았으면 큐에 모두 저장하고 방문처리한다
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
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        visited = new boolean[N+1];
        A = new ArrayList[N+1];
        answer = new int[N+1];

        // 초기화
        for (int i = 01; i <=N; i++) {
            A[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            A[u].add(v);
            A[v].add(u);
        }

        // 오름차순 정렬
        for (int i = 1; i <= N; i++) {
            Collections.sort(A[i]);
        }

        BFS(R); // R부터 BFS 수행

        // 출력
        for (int i = 1; i < answer.length; i++) {
            sb.append(answer[i]).append("\n");
        }

        System.out.println(sb);
    }
}
