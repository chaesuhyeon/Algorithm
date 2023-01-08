package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.StringTokenizer;

// 문제 : https://www.acmicpc.net/problem/1012 - 유기농 배추
// 알고리즘 : dfs
public class ex_1012 {
    public static int T,M,N,K;
    public static int[][] graph;

    public static boolean dfs(int x , int y){

        if(x < 0 || x >=M || y < 0 || y >= N ){
            return false;
        }

        if(graph[x][y] == 1){
            graph[x][y] = 0;
            dfs(x+1, y);
            dfs(x-1, y);
            dfs(x, y+1);
            dfs(x, y-1);
            return true;
        }

        return false;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            graph = new int[M][N];
            int count = 0;

            for (int j = 0; j < K; j++) {
                st = new StringTokenizer(br.readLine());
                int X = Integer.parseInt(st.nextToken());
                int Y = Integer.parseInt(st.nextToken());

                graph[X][Y] = 1;
            }

            for (int x = 0; x < M; x++) {
                for (int y = 0; y < N; y++) {
                    if(dfs(x,y)){
                        count +=1;
                    }
                }
            }

            System.out.println(count);
        }

    }
}
