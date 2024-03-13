import java.util.Arrays;

public class Remove_Duplicates_Array {
    public static int removeDuplicates(int[] nums) {
        int num = nums[0];
        int count = 0;

        for (int i = 1, j=1; i < nums.length; i++) {
            if (nums[i] == num) {
                count += 1;
            } else {
                nums[j] = nums[i];
                num = nums[j];
                j++;
            }
        }

        return nums.length - count;
    }
    
    public static void main(String[] args) {
        System.out.println(removeDuplicates(new int[]{1,1,2}));
        System.out.println(removeDuplicates(new int[]{0,0,1,1,1,2,2,3,3,4}));
    }
}
