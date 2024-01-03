class Solution {
    public void moveZeroes(int[] nums) {
        
        int index =0;
        
        for (int i =0;i<nums.length;i++){
            while (index<i && nums[index]!=0){
                index++;
            }
            
            if(nums[index]==0 && nums[i]!=0){
                int temp = nums[index];
                nums[index] = nums[i];
                nums[i] = temp;
            }
        }
    }
}