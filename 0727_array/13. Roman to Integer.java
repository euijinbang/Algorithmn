class Solution {
    public int romanToInt(String s) {

        HashMap<Character, Integer> roman = new HashMap<Character, Integer>();
        roman.put('M', 1000);
        roman.put('D', 500);
        roman.put('C', 100);
        roman.put('L', 50);
        roman.put('X', 10);
        roman.put('V', 5);
        roman.put('I', 1);

        int result = 0;

        for (int i = 0; i < s.length() - 1; i++) {
            // 예외의 경우
            if (roman.get(s.charAt(i)) < roman.get(s.charAt(i+1))) {
                result -= roman.get(s.charAt(i));
            }
            else {
                result += roman.get(s.charAt(i));
            }
        }

        // 마지막 수는 항상 더한다.
        return result + roman.get(s.charAt(s.length()-1));

    }
}