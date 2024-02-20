class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def helper(idx,arr):
            if idx == 1:
                return arr.append([1])
            
            helper(idx-1,arr)
            curr = [1]
            prev = arr[-1][0]
            for i in range(1,len(arr[-1])):
                prev += arr[-1][i]
                curr.append(prev)
                prev = arr[-1][i]
            curr.append(1)
            arr.append(curr)
        arr = []
        helper(numRows,arr)
        return arr


        