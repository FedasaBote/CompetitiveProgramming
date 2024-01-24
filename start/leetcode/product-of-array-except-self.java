class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] forward=new int[nums.length];
        int [] reverse =new int[nums.length];
        for(int i=0;i<nums.length;i++){
            if(i==0){
                forward[i]=1;
                reverse[nums.length-1]=1;
            }
            else{
                forward[i]=forward[i-1]*nums[i-1];
                reverse[nums.length-1-i]=reverse[nums.length-i]*nums[nums.length-i];
            }
        }

        int[] result=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            if(i==0)
                result[i]=reverse[i];
            else if(i==nums.length-1)
                result[i]=forward[i];
            else
                result[i]=forward[i]*reverse[i];
        }
        return result;

    }
}