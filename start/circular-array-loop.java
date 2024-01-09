class Solution {
    public boolean circularArrayLoop(int[] nums) {
        int n = nums.length;
        
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                continue; // Skip already visited indices or elements with value 0
            }
            
            int slow = i;
            int fast = getNextIndex(nums, i);
            
            while (nums[slow] * nums[fast] > 0 && nums[slow] * nums[getNextIndex(nums, fast)] > 0) {
                if (slow == fast) {
                    if (slow == getNextIndex(nums, slow)) {
                        break; // Single element loop
                    }
                    return true; // Loop found
                }
                
                slow = getNextIndex(nums, slow);
                fast = getNextIndex(nums, getNextIndex(nums, fast));
            }
            
            // Mark the current loop as visited (set all elements to 0)
            int j = i;
            while (nums[j] * nums[getNextIndex(nums, j)] > 0) {
                int next = getNextIndex(nums, j);
                nums[j] = 0;
                j = next;
            }
        }
        
        return false;
    }
    
    private int getNextIndex(int[] nums, int index) {
        int n = nums.length;
        int next = (index + nums[index]) % n;
        
        if (next < 0) {
            next += n;
        }
        
        return next;
    }
}