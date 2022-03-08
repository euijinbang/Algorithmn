import java.util.Scanner;
import java.util.*;

public class BOJ10817 {
    final static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {

        // 새로운 배열을 생성 : 타입[] 변수이름 = new 타입[]
        int[] myArr = new int[3];

        for (int i=0; i<3; i++) {
            myArr[i] = sc.nextInt(); // 공백을 기준으로 하나씩 가져온다.
        }
        sc.close(); 
        // 명시 적으로 close()메소드를 호출하지 않더라도 Closeable 인터페이스가 호출되어 스트림을 닫습니다. 
        // Scanner를 명시 적으로 닫는 것이 좋습니다.

        /*
        int A = sc.nextInt();
        int B = sc.nextInt();   
        int C = sc.nextInt();
        
        int[] myArr = {A, B, C};
        */

        Arrays.sort(myArr);
        System.out.println(myArr[1]);
    }
}