class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:        
        points.sort()
        merged = []
        prev = []
        for idx in range(len(points)):
            if idx == 0:
                merged.append(prev)
                prev = points[0]
            elif prev[1] >= points[idx][0]:
                start = max(prev[0],points[idx][0])
                end = min(prev[1],points[idx][1])
                if merged:
                    merged.pop()
                merged.append([start,end])
                prev = [start,end]
            else:
                prev = points[idx]
                merged.append(prev[:])
               

        return len(merged)

