import java.util.*;

public class BOJ1157 {
    final static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        HashMap map = new HashMap();
        String text = scanner.nextLine();

        String[] arrayTxt;  // String 을 담을 배열 생성
        arrayTxt = text.split("");  // 배열에 한글자씩 저장

        for (String t : arrayTxt) {
            map.put(t.toUpperCase(), 0);
        }

        for (String t : arrayTxt) {
            map.put(t.toUpperCase(), (int)map.get(t.toUpperCase()) + 1);  // get은 객체를 반환함
        }

        maxAlpha(map);
    }

    static void maxAlpha(HashMap map) {
        String maxKey = "";
        int maxVal = 0;

        Set set = map.entrySet();
        Iterator<Map.Entry<String, Integer>> it = set.iterator();

        // map.entrySet() 이 리턴하는 Set 객체의 Iterator를 사용하여 key, value 를 얻는다.
        while (it.hasNext()) {
            Map.Entry<String, Integer> entrySet = (Map.Entry<String, Integer>) it.next();

            if (entrySet.getValue() > maxVal) {
                maxVal = entrySet.getValue();
                maxKey = entrySet.getKey();
            }
            // System.out.println(entrySet.getKey() + ":" + entrySet.getValue());
        }

        int cnt = 0;
        Set<String> keySet = map.keySet();
        for (String key: keySet) {
            if ((int)map.get(key) == maxVal) {
                cnt += 1;
            }
            // System.out.println(key + ":" + map.get(key));
        }

        if (cnt > 1) {
            System.out.println("?");  // 가장 많이 사용된 알파벳이 2개이상 존재시 ? 출력
            return;
        } else {
            System.out.println(maxKey);
        }

    }
}