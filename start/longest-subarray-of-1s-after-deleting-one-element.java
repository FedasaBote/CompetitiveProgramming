class Solution {
    public int longestSubarray(int[] nums) {
        boolean used = false;
        int max = 0, left = 0;

        for (int e = 0; e < nums.length; e++) {
            if (nums[e] == 0) {
                if (used) {
                    while(left<e && nums[left]==1)
                        left+=1;
                    left+=1;
                }
                used = true;
                max = Math.max(max, e - left);
            } else {
                max = Math.max(max, e - left);
            }
        }

        return max;
    }
}