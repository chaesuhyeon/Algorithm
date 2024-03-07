import java.util.HashMap;
import java.util.Map;

public class Roman_To_Integer {
    public static int romanToInt(String s) {
        Map<Character, Integer> map =new HashMap<>();

        map.put('I', 1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);

        char[] charArr = s.toCharArray();
        int result = map.get(charArr[0]);


        for (int i = 1; i < charArr.length; i++) {
            int prev = map.get(charArr[i - 1]);
            int next = map.get(charArr[i]);

            if (prev >= next) {
                result += next; // 1100
            } else {
                result += (next - prev) - prev;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(romanToInt("III"));
        System.out.println(romanToInt("LVIII"));
        System.out.println(romanToInt("MCMXCIV"));
    }
}
