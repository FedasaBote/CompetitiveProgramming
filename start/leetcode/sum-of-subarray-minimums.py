class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = i - stack[-1]
            else:
                left[i] = i + 1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1] - i
            else:
                right[i] = n - i
            stack.append(i)
        res = 0
        for i in range(n):
            res += arr[i] * left[i] * right[i]
        return res % (10 ** 9 + 7)

            