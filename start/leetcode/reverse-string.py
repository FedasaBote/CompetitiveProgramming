class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s)==1:
            return 

        def helper(s,idx):
            n = len(s)
            if idx == len(s)//2 -1:
                s[idx],s[n-1-idx] = s[n-1-idx],s[idx]
                return 
            helper(s,idx +1)
            s[idx],s[n-1-idx] = s[n-1-idx],s[idx]

        helper(s,0)

       
        