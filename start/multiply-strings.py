class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans =''
        p=1
        res =[]
        for i in range(len(num1)-1,-1,-1):
            curr = ""
            rem =0
            for j in range(len(num2)-1,-1,-1):
                val = int(num1[i])*int(num2[j])
                val+=rem
            
                if j==0:
                    curr =str(val)+curr
                    continue
                curr=str(val%10)+curr
                if val>9:
                    rem = val//10
                else:
                    rem =0
            add = str(p).count('0')
            curr+=('0'*add)
            p*=10
            res.append(curr[::-1])
        
        
        n = max(map(lambda x:len(x),res))
        ans =""
        rem =0
        for i in range(n):
            add =0
            for curr in res:
                if i <len(curr):
                    add+=int(curr[i])
                    
            add+=rem
            if i==n-1:
                ans =str(add)+ans
                continue
            ans=str(add%10)+ans
            rem=add//10
        ans =ans.lstrip('0')
        return ans if ans!='' else '0'
            
                    
                
                    
                    
                
                
                
        