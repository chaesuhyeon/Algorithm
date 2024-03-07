class Palindrome_Number {
    public static boolean isPalindrome(int x) {
        String number = String.valueOf(x);
        char[] charArr = number.toCharArray();
        int length = charArr.length;


        for (int i = 0; i < charArr.length; i++) {
            length = length - 1;

            if (charArr[i] != charArr[length]) {
                return false;
            }
        }

        return true;
    }


    public static void main(String[] args) {
        System.out.println(isPalindrome(10));
    }
}