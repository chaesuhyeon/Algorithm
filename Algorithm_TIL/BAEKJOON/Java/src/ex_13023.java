package src;

import java.util.ArrayList;
import java.util.Scanner;

// 문제 : https://www.acmicpc.net/problem/13023 - ABCDE
// 알고리즘 : dfs
public class ex_13023 {
    static int N,M;
    static boolean[] visited ;
    static ArrayList<Integer>[] A;
    static boolean arrive;

    public static void DFS(int x, int depth){
        if(depth == 5 || arrive){
            arrive = true; // depth가 5인 경우에는 arrive = true
            return;
        }
        visited[x] = true;
        for (int i : A[x]) {
            if(!visited[i]){
                DFS(i,depth+1); // DFS 돌 때마다 depth 증가
            }
        }
        visited[x] = false; // depth가 5가 아닐 경우에는 방문 취소(다시 돌아야하기 때문에)
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

         N = sc.nextInt();
         M = sc.nextInt();

         A = new ArrayList[N];
         visited = new boolean[N];
         arrive = false;

        for (int i = 0; i < N; i++) {
            A[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            A[a].add(b);
            A[b].add(a);
        }

        for (int i = 0; i < N; i++) {
            DFS(i, 1); // depth 1부터 시작
            if(arrive) {
                break;
            }
        }

        System.out.println(arrive ? 1 : 0); // depth 5이면 1 아니면 0 출력
    }
}
