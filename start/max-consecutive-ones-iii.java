class Solution {
    public int longestOnes(int[] nums, int k) {
        
        int left=0,max=0;
        for(int end=0;end<nums.length;end++){
            
            if(nums[end]==0)
                k-=1;
            if(k<0)
            {
                if(nums[left]==0)
                    k+=1;
                left+=1;
            }
            
            max = Math.max(max,end -left+1);
        }
        
        return max;
    }
}