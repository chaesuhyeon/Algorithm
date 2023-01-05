public class 점의_위치_구하기 {
    public static void main(String[] args) {
        new 점의_위치_구하기().solution(new int[]{2,4});
    }
    public int solution(int[] dot) {
        int answer = 0;

        if(dot[0] >0 && dot[1] > 0){
            answer = 1;
        } else if(dot[0] <0 && dot[1] > 0){
            answer = 2;
        } else if(dot[0] < 0 && dot[1] < 0){
            answer = 3;
        } else if(dot[0]> 0 && dot[1] < 0){
            answer = 4;
        }

        return answer;
    }

}
