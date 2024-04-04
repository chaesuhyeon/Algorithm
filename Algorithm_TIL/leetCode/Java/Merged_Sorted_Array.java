import java.util.Arrays;

public class Merged_Sorted_Array {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int i = m, j=0; i < nums1.length; i++, j++) {
            nums1[i] = nums2[j];
        }

        Arrays.sort(nums1);
    }

    public static void main(String[] args) {
        merge(new int[]{1,2,3,0,0,0}, 3, new int[]{2,5,6}, 3);
        merge(new int[]{1}, 1, new int[]{}, 0);
        merge(new int[]{0}, 0, new int[]{1}, 1);
    }
}
