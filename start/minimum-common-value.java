class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        
        int l =0;
        int r =0;
        int common =-1;
        while(l< nums1.length && r<nums2.length){
            if (nums1[l]==nums2[r]){
                common = nums1[l];
                break;
            }
            else if(nums1[l]>nums2[r]){
                r++;
            }
            else{
                l++;
            }
        }
        
        return common;
    }
}