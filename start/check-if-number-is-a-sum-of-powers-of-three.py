class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        total =n

        while total>0:
            rem = total%3

            if(rem==2):
                return False

            total//=3

        return True



        