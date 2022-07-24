class S1 {
    public static String solution(String new_id) {

        String answer = "";

        // pointer i
        int i = 0;
        int len = new_id.length();

        while (i < len) {

            char target = new_id.charAt(i);

            if (Character.isAlphabetic(target)) {
                char tmp = new_id.charAt(i);
                if ((65 <= tmp) && (tmp <= 90)) {
                    tmp = Character.toLowerCase(tmp);
                }
                answer += tmp;
            }

            if (Character.isDigit(target) || target == '_' || target == '-') {
                answer += target;
            }

            if (target == '.') {
                answer += '.';
                while (true) {
                    if (i + 1 < new_id.length()) {
                        if (new_id.charAt(i + 1) != '.') {
                            break;
                        }
                        i += 1;
                    } else {
                        break;
                    }
                }
            }

            i += 1;
        }

        // .. 중복삭제
        String answer_no_dup = "";
        for (i = 0; i < answer.length(); i++) {
            if (answer.charAt(i) == '.') {
                answer_no_dup += '.';
                while (true) {
                    if (i + 1 < answer.length()) {
                        if (answer.charAt(i + 1) != '.') {
                            break;
                        }
                        i += 1;
                    } else {
                        break;
                    }
                }
            } else {
                answer_no_dup += answer.charAt(i);
            }
        }

        // 마침표 삭제
        if (answer_no_dup.length() != 0) {
            while (true) {
                if (answer_no_dup.charAt(0) == '.') {
                    answer_no_dup = answer_no_dup.substring(1);
                }
                if (answer_no_dup.length() == 0) break;
                if (answer_no_dup.charAt(answer_no_dup.length() - 1) == '.') {
                    answer_no_dup = answer_no_dup.substring(0, answer_no_dup.length() - 1);
                } else {
                    break;
                }
            }
        }

        // 빈 문자열 검사
        if (answer_no_dup.length() == 0) {
            answer_no_dup += 'a';
        }

        // 길이 검사
        if (answer_no_dup.length() < 3) {
            while (answer_no_dup.length() != 3) {
                answer_no_dup += answer_no_dup.charAt(answer_no_dup.length()-1);
            }
        }

        if (answer_no_dup.length() > 15) {
            answer_no_dup = answer_no_dup.substring(0, 15);
            if (answer_no_dup.charAt(answer_no_dup.length()-1) == '.') {
                answer_no_dup = answer_no_dup.substring(0, answer_no_dup.length()-1);
            }
        }

        return answer_no_dup;
    }
}