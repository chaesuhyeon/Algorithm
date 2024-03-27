
// 다시 풀어보기
public class 모음사전 {
    public static void main(String[] args) {
        System.out.println(new 모음사전().solution("AAAAE"));
    }

    static int answer = 0;
    static boolean[] visited;
    static String[] arr = {"A", "E", "I", "O", "U"};
    static String str = "";
    static void dfs(int count, int depth, String str, String word){
        for (int i = 0; i < word.length(); i++) {
            if(depth == 5){
                return;
            }
            str = str + arr[i];
            if(str.equals(word)){
               answer = count;
            }
            dfs(count+1,depth+1, str , word);

        }
    }

    public int solution(String word) {
        dfs(0,0,"",word);
        return answer;
    }
}
