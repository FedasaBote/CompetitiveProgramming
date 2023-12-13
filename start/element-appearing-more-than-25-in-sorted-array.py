class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        
        count =1
        per = len(arr) / 4
        
        for i in range(1,len(arr)):
            if arr[i-1]==arr[i]:
                count+=1
            else:
                count =1
                
            if count>per:
                return arr[i]
        if count>per:
                return arr[i]
            
            
        
        