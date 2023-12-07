class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        mon = 0
        next_day= 0
        total=0
        for i in range(1,n+1):
            if i%7==1:
                mon+=1
                next_day =mon
            else:
                next_day+=1
                
            total+=next_day
            
        return total
        