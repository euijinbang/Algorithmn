class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
    // x[1] 기준 reverse 정렬
//         Arrays.sort(boxTypes, (a, b) -> b[1] - a[1]);
        Arrays.sort(boxTypes, (a, b) -> Integer.compare(b[1], a[1]);
        int answer = 0;
        for (int[] box : boxTypes) {
            int n = Math.min(box[0], truckSize);
            answer += n * box[1];
            truckSize -= n;
            if (truckSize == 0) break;
        }
        return answer;
    }
}