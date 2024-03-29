class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m={0:1}
        curSum=0
        res=0
        for i in nums:
            curSum+=i
            diff=curSum-k

            res+=m.get(diff,0)
            m[curSum]=m.get(curSum,0)+1
        return res

