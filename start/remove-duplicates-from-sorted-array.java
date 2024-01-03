class Solution {
    public int removeDuplicates(int[] nums) {
        
        int index = 1;
        
        for(int i=0;i<nums.length;i++){
            if(nums[index-1]!=nums[i]){
                int temp = nums[i];
                nums[i] = nums[index];
                nums[index] = temp;
                index ++;
            }
        }
        
        return index;
    }
}