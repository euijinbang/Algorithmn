import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 클래스명 Main 으로 바꾸어 제출할 것!
public class 색종이_1438 {
    public static void main(String[] args) throws IOException {
        // B.R 객체 생성
//        BufferedReader br = new BufferedReader(new FileReader("src/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 이차원 배열 초기화
        Boolean arr[][] = new Boolean[100][100];
        for (int i = 0; i < 100; i++) {
            Arrays.fill(arr[i], false);
        }

        // S.T 객체 생성
        StringTokenizer st = null;
        int n = Integer.parseInt(br.readLine());  // 입력 갯수

        for (int k = 0; k < n; k++) {
            st = new StringTokenizer(br.readLine());  // 공백 기준
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            for (int i = r; i < r + 10; i++) {
                for (int j = c; j < c + 10; j++) {
                    arr[i][j] = true;
                }
            }
        }

        int result = 0;
        for (int q = 0; q < 100; q++) {
            for (int s = 0; s < 100; s++) {
                if (arr[q][s]) {
                    result += 1;
                }
            }
        }

        System.out.print(result);

    }
}
