import java.util.*;

public class 신입사원_1946 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt(); // 테스트 케이스 개수


        for (int i = 0; i < T; i++) {
            List<int[]> list = new ArrayList<>(); // 성적 담을 리스트 초기화
            int count = 1; // 첫번째는 무조건 합격이라서 count를 1로 초기화

            int N = sc.nextInt(); // 지원자 수
            for (int j = 0; j < N; j++) {
                list.add(new int[]{sc.nextInt(), sc.nextInt()}); // 서류심사 성적 순위, 면접 성적 순위 입력 받음
            }

            Collections.sort(list, new Comparator<int[]>() { // 서류심사 성적 순위를 기준으로 오름차순 정렬 (면접 성적의 순위만 비교하기 위해)
                @Override
                public int compare(int[] o1, int[] o2) {
                    return o1[0]-o2[0];
                }
            });

            int score = list.get(0)[1]; // 서류심사 성적 1위 지원자의 면접 성적 순위
            for (int j = 1; j < N; j++) {
                int num = list.get(j)[1]; // 다른 지원자들의 면접 성적 순위
                if (score > num){ // 이미 서류심사 성적 순위에서 밀렸기 때문에 면접 성적 순위는 높아야함
                    count ++; // 면접 순위가 높다면 count + 1 해준다.
                    score = num; // score를 num으로 바꿔줌
                }
            }
            System.out.println(count);
        }

    }
}
