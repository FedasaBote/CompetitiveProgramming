class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        tasks.sort()
        processorTime.sort(reverse = True)
        total = 0
        
        for idx,p in enumerate(processorTime):
            
            total = max(total,p + tasks[idx*4+3])
            
            
        return total