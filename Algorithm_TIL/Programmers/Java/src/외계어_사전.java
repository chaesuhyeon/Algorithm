package src;

public class 외계어_사전 {
    public static void main(String[] args) {
        new 외계어_사전().solution(new String[]{"p", "o", "s"}, new String[]{"sod", "eocd", "qixm", "adio", "soo"});
    }

    public int solution(String[] spell, String[] dic) {
        int answer = 2;


        for(int i=0; i< dic.length; i++){
            if(dic[i].length() == spell.length){
                for(int j=0; j < spell.length; j++){
                    dic[i] = dic[i].replaceFirst(spell[j],"");
                    if(dic[i].equals("")){
                        answer= 1;
                    }
                }
            }
        }

        return answer;
    }
}
