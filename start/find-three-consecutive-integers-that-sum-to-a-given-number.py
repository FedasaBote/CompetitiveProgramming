class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        if num%3!=0:
            return []

        second = num//3

        return [second-1,second,second+1]
        