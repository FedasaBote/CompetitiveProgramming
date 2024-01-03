class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        removed =""
        
        for d in s:
            if d.isalpha() or d.isdigit():
                removed+=d
                
        removed = removed.lower()
        print(removed)
        left = 0
        right = len(removed) -1
        
        while left<=right:
            if removed[left] != removed[right]:
                return False
            
            left+=1
            right-=1
            
        return True
        