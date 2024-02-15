class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        c = 0
        for key in count.keys():
            c += count[key]//2 *2

        if c!= len(s):
            c += 1
        return c
        