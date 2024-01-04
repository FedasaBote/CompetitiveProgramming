class Solution {
    public long dividePlayers(int[] skill) {
        int n = skill.length;
        
        if (n%2 != 0){
            return -1;
        }
        Arrays.sort(skill);
        int l = 0;
        int r =  n -1;
        int total = skill[r] + skill[l];
         
        long chemistry = 0;
        while(l<r){
            if(total != skill[r] + skill[l])
                return -1;
            chemistry += (long)(skill[r] * skill[l]); 
            l+=1;
            r -=1;
           
        }
        
        return chemistry;
    }
}