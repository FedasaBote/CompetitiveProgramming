class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int windowSize = n-k,left = 0;
        int total_sum = Arrays.stream(cardPoints).sum();
        
        if(k==n) return total_sum;
        int cur_sum = 0,ans =0;
        for(int end=0;end<n;end++){
            cur_sum+=cardPoints[end];
            
            if(end >=windowSize-1){
                ans = Math.max(ans,total_sum-cur_sum);
                cur_sum-=cardPoints[left];
                left+=1;
            }
        }
        
        
        return ans;
        
    }
}