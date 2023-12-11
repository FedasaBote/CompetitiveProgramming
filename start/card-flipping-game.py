class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        nums = set(fronts+backs)
        
        for f,b in zip(fronts,backs):
            if f==b and f in nums:
                nums.remove(f)
                
        return min(nums) if nums else 0
        