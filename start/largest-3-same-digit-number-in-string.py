class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        count =1
        ans =''
        for i in range(1,len(num)):
            if num[i-1]==num[i]:
                count+=1
            else:
                count =1
            if count==3:
                ans = max(ans,num[i-2:i+1])
                count=0
                
        return ans
                
                
            
            
        