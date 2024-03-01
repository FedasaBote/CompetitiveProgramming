class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        if k ==1 or k == len(weights):
            return 0

        score =[0]*(len(weights)-1)
        for i in range(len(weights)-1):
            score[i]= weights[i] + weights[i+1]

        score.sort()
        min_sum =0
        max_sum = 0

        for i in range(k-1):
            min_sum += score[i]
            max_sum += score[len(score) -i - 1]

        return max_sum - min_sum
        
