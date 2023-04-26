package src;

public class 카펫 {
    public static void main(String[] args) {
        System.out.println(new 카펫().solution(10,2));
    }

    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int sum = brown + yellow;

        for (int i = 3; i < sum; i++) { // 가로와 세로 모두 길이가 3 이상이어야 yellow를 가운데 넣을 수 있음
            int j = sum / i;

            if(sum % i == 0 && j >=3){ // 가로와 세로 모두 길이가 3 이상이어야 yellow를 가운데 넣을 수 있음
                int col = Math.max(i,j); // 가로가 더 길어아 함
                int row = Math.min(i,j); // 세로는 짧아야 함
                int center = (col - 2) * (row - 2);

                if(center == yellow){ // center 값이랑 yellow 개수랑 같다면 카펫 모양이 만들어 질 수 있음
                    answer[0] = col; // 이때의 가로, 세로 answer 배열에 대입
                    answer[1] = row;
                }
            }

        }
        return answer;
    }
}
