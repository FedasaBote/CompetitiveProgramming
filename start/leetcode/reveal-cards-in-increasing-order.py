class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = []
        
        for i in range(len(deck) - 1, -1, -1):
            if queue:
                queue.insert(0, queue.pop())
            queue.insert(0, deck[i])
        
        return queue
        