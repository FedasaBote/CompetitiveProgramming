class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        combo= []
        ans = []

        def helper(idx):
            if len(combo) == k:
                if sum(combo) == n:
                    ans.append(combo[:])

                return
            if idx == 10:
                return

            combo.append(idx)
            helper(idx +1)
            combo.pop()
            helper(idx +1)
        helper(1)
        return ans
        