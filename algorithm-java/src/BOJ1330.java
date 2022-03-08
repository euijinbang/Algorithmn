import java.util.Scanner;

public class BOJ1330 {
    final static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int A = scanner.nextInt();
        int B = scanner.nextInt();

        if (A > B) {
            System.out.println(">");
        } else if (A < B) {
            System.out.println("<");
        } else {
            System.out.println("==");
        }
    }
}
