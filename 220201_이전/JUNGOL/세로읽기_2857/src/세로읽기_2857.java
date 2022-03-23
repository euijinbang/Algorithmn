import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.FileReader;
import java.util.Arrays;

//public class Main {
public class 세로읽기_2857 {
    public static void main(String[] args) throws IOException {

//        BufferedReader in = new BufferedReader(new FileReader("src/input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        char arr[][] = new char [5][15];

        for (int i = 0; i < 5; i++) {
            String s = in.readLine();

            // .charAt(idx) 특정 인덱스의 문자열을 반환
            for (int j = 0; j < s.length(); j++) {
                arr[i][j] = s.charAt(j);
            }
        }
//        System.out.println(Arrays.deepToString(arr));

        for (int i = 0; i < 15; i++) {
            for (int j = 0; j < 5; j++) {
                if (arr[j][i] == '\0') continue;
                System.out.print(arr[j][i]);
            }
        }
    }
}
