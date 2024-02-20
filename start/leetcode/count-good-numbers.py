class Solution:
    def countGoodNumbers(self, n: int) -> int:

        odd = n //2
        even = n - odd
        mod = 10**9 + 7

        return int(self.modularExponentiation(4,odd,mod) *  self.modularExponentiation(5,even,mod))%mod

    def modularExponentiation(self,base,exponent,mod):
        if exponent == 0:
            return 1
        halfResult = self.modularExponentiation(base, exponent // 2, mod) % mod
        result = (halfResult * halfResult) % mod
        if (exponent % 2 == 1):
            result = (result * base) % mod
        return result



            