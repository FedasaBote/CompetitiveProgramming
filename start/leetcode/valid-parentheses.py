class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """ 
        arr=[]
        if (len(s)%2!=0):return False
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                arr.append(i)
            elif s[i]==")" and len(arr)>0 and s[arr[-1]]=="(":
                arr.pop()
            elif s[i]=="]" and len(arr)>0 and s[arr[-1]]=="[":
                arr.pop()
            elif s[i]=="}" and len(arr)>0 and s[arr[-1]]=="{":
                arr.pop()
            else:return False
        
        return len(arr)==0
      