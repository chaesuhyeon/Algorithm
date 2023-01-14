import java.util.ArrayList;
import java.util.List;

public class 주식가격 {
    public static void main(String[] args) {
        new 주식가격().solution(new int[] {1,2,3,2,3});
    }

    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];

        for(int i=0; i < prices.length; i++){
            for(int j=i+1; j < prices.length; j++){
                if(prices[i] <= prices[j]){ // 본인 제외하고 자기보다 큰 숫자가 몇개있는지 센다
                    answer[i] ++;
                } else { // 자기보다 작으면 뒤에껄 더 볼 필요가 없으므로 개수1개 증가시키고 break건다.
                    answer[i] ++;
                    break;
                }
            }
        }

        return answer;
    }
}
