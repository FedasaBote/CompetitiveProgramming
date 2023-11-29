class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False

        temp =x
        reversed =0

        while x>0:
            rem = x%10
            reversed = reversed*10 + rem
            x= x//10

        return reversed==temp
        