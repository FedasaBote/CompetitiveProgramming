class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """

        total = n
        while (True):
            if total%2==0:
                return total
            total+=n


        