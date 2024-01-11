class Solution {
    public double findMaxAverage(int[] nums, int k) {
        
        double total =0;
        double ans = Integer.MIN_VALUE;
        for (int i=0;i<nums.length;i++){
            total+=(double)nums[i]/k;
            
            if(i>=k-1){
                ans = Math.max(ans,total);
                total-=(double)nums[i-k+1]/k;
            }
        }
        
        return ans;
    }
}