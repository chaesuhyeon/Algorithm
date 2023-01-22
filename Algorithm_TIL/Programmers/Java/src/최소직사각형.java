package src;

public class 최소직사각형 {
    public static void main(String[] args) {
        System.out.println(new 최소직사각형().solution(new int[][]{{60,50},{30,70},{60,30},{80,40}}));
    }
    public int solution(int[][] sizes) {
        int answer = 0;
        int w = 0;
        int h = 0;

        for (int i = 0; i < sizes.length; i++) {
            if(sizes[i][0] > w){
                w = sizes[i][0];
            }

            if(sizes[i][1] > h){
                h = sizes[i][1];
            }
        }

        for (int i = 0; i < sizes.length; i++) {
            
        }
        return answer;
    }
}
