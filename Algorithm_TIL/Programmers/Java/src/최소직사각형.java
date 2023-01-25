package src;

public class 최소직사각형 {
    public static void main(String[] args) {
        System.out.println(new 최소직사각형().solution(new int[][]{{60,50},{30,70},{60,30},{80,40}}));
    }
    public int solution(int[][] sizes) {
        int answer = 0;
        int w = 0;
        int h = 0;
        int w_max = 0;
        int h_max = 0;

        for (int i = 0; i < sizes.length; i++) {
            for (int j = 0; j < sizes[i].length; j++) {
                w = Math.max(sizes[i][0] , sizes[i][1]); // 가로와 세로 중에서 긴 길이를 가로로 구함
                h = Math.min(sizes[i][0] , sizes[i][1]); // 가로와 세로 중에서 작은 길이를 세로로 구함 (세로가 더 길면 가로 세로 바꿔줘야하기 때문)
            }

            w_max = Math.max(w_max , w); // 가로의 길이 : 가로중에서 제일 긴 길이
            h_max = Math.max(h_max, h); // 세로의 길이 : 세로 중에서 제일 긴 길이 (가로 세로 교환 후에 제일 긴 길이)
        }

        answer = w_max * h_max; // 두 수를 곱함
        return answer;
    }
}
