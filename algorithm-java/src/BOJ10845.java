import java.io.*;
import java.util.Arrays;
import java.util.LinkedList;

/*
큐 구현하기
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
*/

// 제출시 클래스명 Main 으로 수정

public class BOJ10845 {
    static void push(LinkedList<Integer> ll, int x) {
        ll.offer(x);  // 링크드리스트 끝에 객체를 추가
    }

    static void pop(LinkedList<Integer> ll) {
        if (ll.size() != 0) {
            System.out.println(ll.poll());  // pop() : 링크드리스트의 첫 번째 요소를 반환후 제거
        } else {
            System.out.println(-1);
        }
    }

    static void size(LinkedList<Integer> ll) {
        System.out.println(ll.size());
    }

    static void empty(LinkedList<Integer> ll) {
        if (ll.size() != 0) {
            System.out.println(0);
        } else {
            System.out.println(1);
        }
    }

    static void front(LinkedList<Integer> ll) {
        if (ll.size() != 0) {        // peek() : 링크드리스트의 첫번째 요소를 반환
            System.out.println(ll.peek());
        } else {
            System.out.println(-1);
        }
    }

    static void back(LinkedList<Integer> ll) {
        if (ll.size() != 0) {
            System.out.println(ll.getLast()); // getLast() : 링크드리스트의 마지막 요소를 반환
        } else {
            System.out.println(-1);
        }
    }

    static BufferedReader bf;

    public static void main(String[] args) throws IOException {
        LinkedList<Integer> ls = new LinkedList<Integer>();

//        File path = new File(".");
//        System.out.println(path.getAbsolutePath());

        try {
            bf = new BufferedReader(new InputStreamReader(System.in)); // 제출용

            int totalNum = Integer.parseInt(bf.readLine());

            for (int i = 0; i < totalNum; i++) {
                String s = bf.readLine();
                String[] ar = s.split(" ");
                String order = ar[0];

                if (ar.length != 1) {
                    int num = Integer.parseInt(ar[1]);
                    push(ls, num);
                }

                switch (order) {
                    case "front":
                        front(ls);
                        break;
                    case "back":
                        back(ls);
                        break;
                    case "pop":
                        pop(ls);
                        break;
                    case "size":
                        size(ls);
                        break;
                    case "empty":
                        empty(ls);
                        break;
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
