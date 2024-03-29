class Solution {
    public int maxCoins(int[] piles) {
         int n=piles.length, M=0;
        int [] freq=new int[10001];
    //    Arrays.fill(freq, 0);
        for (int x : piles){
            freq[x]++;
            M=Math.max(M, x);
        }
        int ans=0, count=0, x=0, alice=0, k=n/3;
        for(x=M; count<k; x--){
            if (freq[x]>0){
                int f=freq[x]+alice;
                int f0=f>>1;
                count+=f0;
                ans+=f0*x;
                alice=(f%2==1)?1:0;
            }
        }
        ans-=(count-k)*(x+1);//if count>n/3 subtract some piles
        return ans;
    }
}