class Solution:
    def smallestNumber(self, num: int) -> int:
        
        neg = num < 0
        num = list(str(abs(num)))
        num.sort()
        zeros = num.count("0")
        if zeros <len(num):
            p = num[zeros] + "0"*zeros +"".join(num[zeros+1:])
        else:
            p = "0"*zeros
        n = "".join(num[zeros:][::-1]) + "0"*zeros
        
        if neg:
            return -int(n)
        else:
            return int(p)
        