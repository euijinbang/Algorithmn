import java.util.ArrayList;
import java.util.Scanner;

public class BOJ10773 {
    final static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        final int LIMIT = 100000;
        int K = scanner.nextInt();

        ArrayList<Integer> data = new ArrayList<Integer>(LIMIT);

        for (int i = 0; i < K; i++) {
            int n = scanner.nextInt();

            if (n == 0) {
                data.remove(data.size() - 1); // pop()
            } else {
                data.add(n);
            }
        }
        int total = data.stream().mapToInt(Integer::intValue).sum(); // stream
        System.out.println(total);
    }
}