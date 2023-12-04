class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans =[False]*len(candies)
        max_ = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max_:
                ans[i]=True
                
        return ans
        