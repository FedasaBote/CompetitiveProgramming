class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr)<3:
            return False
        l = 0
        r = len(arr) -1
        while  l<len(arr)-1 and arr[l]<arr[l+1]:
            l+=1
            
        while r > 0 and arr[r]<arr[r-1]:
            r-=1
        
        return r==l and r<len(arr)-1 and l>0
            