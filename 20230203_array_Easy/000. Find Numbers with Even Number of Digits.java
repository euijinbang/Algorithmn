class Solution {
    public int findNumbers(int[] nums) {
        int even = 0;
        for(int num : nums) {
            int digit = 1;
            while((num / 10) > 0) {
                digit += 1;
                num = num / 10;
            }
            if(digit % 2 == 0) {
                even += 1;
            }
        }
        return even;
    }
}