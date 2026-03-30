class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int max = nums[0]; // -2
        int min = nums[0]; // -2
        int curMaxSum = nums[0]; // -2
        int curMinSum = nums[0]; // -2
        int sum = nums[0]; // -2

        for (int i = 1; i < nums.length; i++) {
            // -3, -1
            sum += nums[i]; // -5, -6

            curMaxSum = Math.max(curMaxSum + nums[i], nums[i]); // -3, -1
            curMinSum = Math.min(curMinSum + nums[i], nums[i]); // -5, -6 

            max = Math.max(max, curMaxSum); // -2
            min = Math.min(min, curMinSum); // -5
        }
        if (sum == min) return max;
        return Math.max(sum - min, max);
    }
}
// max       -2 4.  4 4. 4. 9. 13
// min       -2 -2 -5 -5 -5 -5 -5 
// curMaxSum -2 4  -1 4  -1 9  13
// curMinSum -2 2. -5 -1 -5 4. 4
// sum       -2 2  -3 1  -4 5  9 