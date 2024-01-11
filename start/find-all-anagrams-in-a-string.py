class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pd,sd={},{}
        l=0
        res=[]
        if len(p)>len(s): return res
        for i in range(len(p)):
            pd[p[i]]=pd.get(p[i],0)+1
            sd[s[i]]=sd.get(s[i],0)+1
        if pd==sd:
           res.append(0)
        for i in range(len(p),len(s)):
            sd[s[l]]=sd[s[l]]-1
            if( sd[s[l]]==0):
                sd.pop(s[l])
            
            sd[s[i]]=sd.get(s[i],0)+1
            l+=1
            if pd==sd:
                res.append(l)
            
        return res



        