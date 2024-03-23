public class Find_The_Index_Of_First {

    public static int strStr(String haystack, String needle) {

        return haystack.indexOf(needle);
    }

    public static void main(String[] args) {
        System.out.println(strStr("sadbutsad", "sad"));
        System.out.println(strStr("leetcode", "leeto"));
    }
}
