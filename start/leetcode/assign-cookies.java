class Solution {
    public int findContentChildren(int[] g, int[] s) {
        
        Arrays.sort(g);
        Arrays.sort(s);
        int num = 0;
        for (int i =0;num<g.length&&i<s.length;i++){

            if (s[i]>=g[num]){
                num++;
            }
           
          
        }
        
        return num;
    }
}