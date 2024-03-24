public class Length_Of_Last_Word {

    public static int lengthOfLastWord(String s) {
        String[] split = s.split(" ");
        return  split[split.length-1].length();
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLastWord("Hello World"));
    }
}
