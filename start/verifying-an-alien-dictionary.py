class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        prev = words[0]
        for word in words[1:]:
            for i in range(min(len(prev),len(word))):
                if order.index(word[i])< order.index(prev[i]):
                    return False
                elif order.index(word[i])> order.index(prev[i]):
                           break
                           
                if len(prev)> len(word) and i==len(word)-1:
                           return False
                           
            prev = word
            
            
        return True
        