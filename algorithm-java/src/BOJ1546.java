import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BOJ1546 {
    public static Scanner sc = new Scanner(System.in);

    private static double newAvgScore(int N, ArrayList scores) {

        int M = 0;
        for (int i = 0; i < N; i++) {
            if ((Integer)scores.get(i) > M) {
                M = (Integer)scores.get(i);
            }
        }

        List<Double> newScore = new ArrayList<>();
        double sum = 0.0;
        for (int i = 0; i < N; i++) {
            double score = (int)scores.get(i) * 1.0;
            newScore.add(score / M * 100);
            sum += score / M * 100;
        }

        double avg = sum / N;

        return avg;
    }

    public static void main(String[] args) {
        int N = sc.nextInt();
        ArrayList<Integer> scores = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            scores.add(sc.nextInt());
        }

        System.out.println(newAvgScore(N, scores));
    }
    }
