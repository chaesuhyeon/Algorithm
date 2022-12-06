import java.util.Stack;

public class 같은_숫자는_싫어 {
    public static void main(String[] args) {
        new 같은_숫자는_싫어().solution(new int[]{1,1,3,3,0,1,1});
    }

    public int[] solution(int []arr) {

        Stack<Integer> st = new Stack<>();
        for(int i=0; i < arr.length; i++){
            if(st.isEmpty()){
                st.push(arr[i]);
            } else if(st.size()>0 && st.peek() == arr[i]){
                continue;
            } else{
                st.push(arr[i]);
            }
        }
        int[] answer = new int[st.size()];
        int i=0;
        for(Integer s : st){
            answer[i] = s;
            i++;
        }


        return answer;
    }
}
