import java.util.Scanner;

public class BOJ1152 {
    final static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String str = scanner.nextLine();
        String[] strList = str.split(" ");
        // System.out.println(str);    // The Curious Case of Benjamin Button
        // System.out.println(strList.length);    // 공백까지 세어버린다.

        int cnt = 0;
        for (String st : strList) {
            if (!st.isEmpty()) {        // 비어있지 않은 경우에만 센다.
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }
}
