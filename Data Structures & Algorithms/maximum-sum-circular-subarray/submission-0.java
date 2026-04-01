class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int max = nums[0];
        int min = nums[0];
        int curMaxSum = nums[0];
        int curMinSum = nums[0];
        int sum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            sum += nums[i];

            curMaxSum = Math.max(curMaxSum + nums[i], nums[i]);
            curMinSum = Math.min(curMinSum + nums[i], nums[i]);

            max = Math.max(max, curMaxSum);
            min = Math.min(min, curMinSum);
        }
        
        return Math.max(sum - min, max);
    }
}
// max       -2 4.  4 4. 4. 9. 13
// min       -2 -2 -5 -5 -5 -5 -5 
// curMaxSum -2 4  -1 4  -1 9  13
// curMinSum -2 2. -5 -1 -5 4. 4
// sum       -2 2  -3 1  -4 5  9 