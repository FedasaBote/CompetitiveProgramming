class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        
        m = {}
        
        for num in nums2:
            m[num] = m.get(num,0)+1
            
        ans = []
        
        for num in nums1:
            if num in m:
                ans.append(num)
                m[num]-=1
                if m[num] ==0:
                    del m[num]
                    
        return ans