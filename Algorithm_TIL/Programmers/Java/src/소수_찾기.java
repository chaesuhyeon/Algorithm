package src;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42839
// 알고리즘 : 브루트포스
public class 소수_찾기 {

    public static void main(String[] args) {
        System.out.println(new 소수_찾기().solution("17"));
    }
    static HashSet<Integer> set = new HashSet<>();
    static char[] arr;
    static boolean[] visited;
    public int solution(String numbers) {
        int answer = 0;
        arr = new char[numbers.length()];
        visited = new boolean[numbers.length()];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = numbers.charAt(i);
        }

        recursion("",0);
        answer = set.size();

        return answer;
    }

    // 백트래킹
    static void recursion(String str, int idx){
        int num = 0;
        if(!str.isEmpty()){
            num = Integer.parseInt(str);
            if(isPrime(num)){ // 소수라면 set에 넣어줌
                set.add(num);
            }
        }

        if(idx == arr.length) return; // 재귀 종료 조건

        for (int i = 0; i < arr.length; i++) {
            if(visited[i]) continue; // 방문한 노드면 넘어감
            visited[i] = true; // 방문 안했으면 방문 처리
            recursion(str + arr[i] , idx + 1); // 모든 조합을 다 찾기 위해 재귀
            visited[i] = false; // 다른 조합도 찾아야 하므로 방문 false
        }
    }

    // 소수 판단
    static boolean isPrime(int num){
        if( num<2) return false;
        for (int i = 2; i < Math.sqrt(num); i++) {
            if(num % i == 0){
                return false;
            }
        }
        return true;

    }
}
