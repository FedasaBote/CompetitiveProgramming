public class Solution {
    public int FindMin(int[] nums) {
        int n = nums.Length;
        int leftIndex = 0, rightIndex = n - 1;

        while (leftIndex < rightIndex) {
            int midIndex = leftIndex + (rightIndex - leftIndex) / 2;
            int prevIndex = midIndex > 0 ? midIndex - 1 : n - 1;
            int nextIndex = midIndex < n - 1 ? midIndex + 1 : 0;

            if (nums[prevIndex] >= nums[midIndex] && nums[midIndex] <= nums[nextIndex]) {
                return nums[midIndex];
            } else if (nums[leftIndex] <= nums[midIndex] && nums[midIndex] <= nums[rightIndex]) {
                return nums[leftIndex];
            } else if (nums[midIndex] < nums[rightIndex]) {
                rightIndex = midIndex;
            } else {
                leftIndex = midIndex + 1;
            }
        }

        return nums[leftIndex];
    }
}
