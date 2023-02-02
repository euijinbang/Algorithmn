import java.util.*;


public class T0521_3 {

    public static void add(List<Integer> tmp, int num, int n, int N, int count) {
        System.out.println(tmp);
        if (n == N) {
            int sum = 0;
            for (int i = 0; i < tmp.size(); i++) {
                System.out.println(tmp.get(i));
                sum += tmp.get(i);
            }
            if (sum != 9) {
                count += 1;
            }
            return;
        }
        tmp.add(num);
        n = tmp.size();
        for (int num = 1; num <= 9; num++) {
            add(tmp, num + 1, n + 1, N, count);
        }
    }

    public static void main(String args[]) {
        List<Integer> tmp = new ArrayList();
        int count = 0;
        int N = 2;
        add();

        System.out.println(count);
    }
}