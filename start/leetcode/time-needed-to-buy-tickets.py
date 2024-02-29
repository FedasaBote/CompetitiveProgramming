class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:


        i = 0
        total_time = 0
        while tickets[k] > 0:
            if tickets[i] == 0:
                i = (i+1) % len(tickets)
                continue

            tickets[i] -= 1
            i = (i+1) % len(tickets)
            total_time += 1

        return total_time

        