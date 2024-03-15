import java.util.Arrays;

public class Plus_One {

    public static int[] plusOne(int[] digits) {
        int n = digits.length;

        for (int i = n - 1; i >= 0; i--) {
            digits[i]++;
            if (digits[i] < 10) {
                return digits;
            }
            digits[i] = 0;
        }

        int[] result = new int[n + 1];
        result[0] = 1;
        return result;
    }

    public static void main(String[] args) {
        System.out.println(plusOne(new int[]{1, 2, 3}));
        System.out.println(plusOne(new int[]{9}));
        System.out.println(plusOne(new int[]{9,8,7,6,5,4,3,2,1,0}));
        System.out.println(plusOne(new int[]{7,2,8,5,0,9,1,2,9,5,3,6,6,7,3,2,8,4,3,7,9,5,7,7,4,7,4,9,4,7,0,1,1,1,7,4,0,0,6}));

    }
}
