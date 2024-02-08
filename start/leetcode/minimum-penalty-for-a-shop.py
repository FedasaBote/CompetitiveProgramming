class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pre_sum = [0]* n
        # pre_sum[0] =1 if customers[0] =="N" else 0
        suf_sum = [0]*n
        suf_sum[-1] =1 if customers[-1] =="Y"  else 0
        
        for i in range(1,n):
            one = 1 if customers[i-1] =="N" else 0
            zero = 1 if customers[n-i-1] =="Y" else 0
            pre_sum[i] = pre_sum[i-1] + one
            suf_sum[n-i-1] = suf_sum[n-i] + zero
        
    
        pre_sum.append(pre_sum[-1])
        suf_sum.append(0)
        
        ans = float('inf')
        res = n
        
        for i in range(n+1):
            curr = pre_sum[i] + suf_sum[i]
    
            if ans > curr:
                ans = curr
                res = i
                
        return res
        