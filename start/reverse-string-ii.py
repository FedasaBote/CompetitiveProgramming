class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        n=len(s)
        if k>n:
            return s[-1::-1]
        l, r, rem = 0, k, n
        s=s[k-1::-1]+s[k:]
        l+=2*k
        r=l+k-1
        rem=n-l
        while l<=n:
            if k>rem:
                s=s[:l]+s[-1:l-1:-1]
                return s
            if rem>=k and rem<2*k:
                s=s[:l]+s[r:l-1:-1]+s[r+1:]
                return s
            s=s[:l]+s[r:l-1:-1]+s[r+1:]
            l+=2*k
            r=l+k-1
            rem=n-l
        return s
            
            
            