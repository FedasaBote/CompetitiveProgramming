class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        m={}
        def negative(x,n):
            if n==-1:
                return 1/x
            if n in m:
                return m[n]
            if n%2==0:
                m[n]=negative(x,n/2)**2
            else:
                m[n]=negative(x,n/2)**2*x
            return m[n] 
        def positive(x,n):
            if n==1:
                return x
            if n in m:
                return m[n]
            if n%2==0:
                m[n]=positive(x,n/2)**2
            else:
                m[n]=positive(x,n/2)**2*x
            return m[n] 
        if n>0:
            return positive(x,n)
        else:
            return negative(x,n)