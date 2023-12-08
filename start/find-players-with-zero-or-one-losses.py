class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        loses ={}
        
        for match in matches:
            loses[match[1]] = loses.get(match[1],0)+1
            
        win = set()
        lose =[]
        
        for match in matches:
            if match[0] not in loses:
                win.add(match[0])
                
            if loses[match[1]]==1:
                lose.append(match[1])
        
        win = list(win)
        win.sort()
        lose.sort()
        return [win,lose]
        