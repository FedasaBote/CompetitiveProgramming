class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        
        int l =0;
        int r = nums.length-1;
        int op =0;
        while(l<r){
            if (nums[l]+nums[r]==k){
                l+=1;
                r-=1;
                op+=1;
            }
            else if(nums[l]+nums[r]>k){
                r-=1;
            }else{
                l+=1;
            }
        }
        
        return op;
    }
}