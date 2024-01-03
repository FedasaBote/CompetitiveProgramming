class Solution {
    public int maxIceCream(int[] costs, int coins) {
        
        int max = Arrays.stream(costs).max().getAsInt(); 
        int index =0;
        int[] nums = new int[max+1];
        
        for(int i =0;i<costs.length;i++){
            nums[costs[i]]++;
        }
        
        for(int i=0;i<nums.length;i++){
            int cnt = nums[i];
            while(cnt>0){
                costs[index]=i;
                index++;
                cnt--;
            }
        }
        
        int ans = 0;
        int i =0;
        while(i<costs.length && coins>0){
            if(coins>=costs[i])
                ans++;
            coins-=costs[i];
            i++;
        }
        
        return ans;
        
    }
}