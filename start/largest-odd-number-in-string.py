class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        back=len(num)
        
        for i in num[::-1]:
            if int(i)%2!=0:
                 break
            back-=1
            
        return num[:back]
            
        