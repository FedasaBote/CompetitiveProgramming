class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dicFruits={}
        first=0
        ans=0
        for i in range(len(fruits)):
            dicFruits[fruits[i]]=dicFruits.get(fruits[i],0)+1
            if len(dicFruits)>2:
                dicFruits[fruits[first]]-=1
                if(dicFruits[fruits[first]]==0):
                    dicFruits.pop(fruits[first])
                first+=1
            ans=max(ans,i-first+1)
        return ans

