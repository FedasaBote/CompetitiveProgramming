class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        costs.sort(key=lambda x: x[0]-x[1])
        total_cost = sum(c[0] for c in costs[:n//2]) + sum(c[1] for c in costs[n//2:])
        return total_cost
