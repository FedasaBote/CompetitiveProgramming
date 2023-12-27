class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        
        m = {}
        
        for idx, val in enumerate(arr2):
            m[val] = idx
            
        for idx, val in enumerate(arr1):
            if val not in m:
                m[val] = len(arr1)+val
            
        def comp(val):
            return m[val]
      
        
        
        arr1.sort(key = comp)
        
        return arr1