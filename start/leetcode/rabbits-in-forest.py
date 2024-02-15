class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        answers.sort()
        c = 0
        i = 0
        
        while i < len(answers):
               
            c += answers[i] + 1
            for j in range(answers[i]):
                if i<len(answers)-1 and answers[i]==answers[i+1]:
                    i += 1
                else:
                    break
            i+=1

        return c

