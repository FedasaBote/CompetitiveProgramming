class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
     int total_sum = 0,count= 0;
     int[] prefix_sum =new int[nums.length+1];
     prefix_sum[0] = 1;
        
    for(int end=0;end<nums.length;end++){
        total_sum+=nums[end];
        if (total_sum>=goal)
            count+=prefix_sum[total_sum-goal];
        
        prefix_sum[total_sum]+=1;

    }

    return count;
     
    }
}