class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = [x for x in s]
        for i,v in enumerate(indices):
            ans[v] = s[i]
     
        return "".join(ans)
            