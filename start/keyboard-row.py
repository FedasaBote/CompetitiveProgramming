class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["qwertyuiopQWERTYUIOP","asdfghjklASDFGHJKL","zxcvbnmZXCVBNM"]
        res = []
        for word in words:
            if len(word)==1:
                res.append(word)
                continue
            i = 1
            while i < len(word) and ((word[i-1] in rows[0] and word[i] in rows[0]) or (word[i-1] in rows[1] and word[i] in rows[1]) or (word[i-1] in rows[2] and word[i] in rows[2])):
                i+=1
                    
            if i == len(word):
                res.append(word)
                
        return res