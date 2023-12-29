class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        num = digits[0]
        
        for i in range(1,len(digits)):
            num *= 10
            num += digits[i]
            
        num += 1
        
        return list(map(int,list(str(num))))