def solve(n, k):
    if n == 0:
        return []

    nums = [-1] * n
    if k < n:
        if k > 0:
            nums[k - 1] = 200
        nums[k] = -400
    else:
        nums = solve(n - 1, k - n)
        nums.append(1000)
    
    return nums

t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  ans = solve(n, k)
  print(*ans)


