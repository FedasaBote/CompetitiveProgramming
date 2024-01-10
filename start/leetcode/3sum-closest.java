class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int closest = nums[0]+nums[1]+nums[2];
        
        for(int i=0;i<nums.length-2;i++){
            int j=i+1;
            int k = nums.length -1;
            
            while(j<k){
                int ans = nums[i]+nums[j]+nums[k];
                
                if(Math.abs(target-closest)>Math.abs(target-ans)){
                    closest = ans;
                }
                
                if(ans==target){
                    return target;
                }
                
                else if(ans>target){
                    k--;
                }
                else{
                    j++;
                }
            }
        }
        
        return closest;
    }
}