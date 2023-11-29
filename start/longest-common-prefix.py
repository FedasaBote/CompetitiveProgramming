class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=strs[0]
        for i in range(1,len(strs)):
            
            j=0
            while  j<len(res) and j<len(strs[i]) and res[j]==strs[i][j]:
                j+=1
            res=res[:j]
        return res
        