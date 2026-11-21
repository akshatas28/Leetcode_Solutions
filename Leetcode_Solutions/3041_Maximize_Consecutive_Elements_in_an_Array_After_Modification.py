from collections import defaultdict
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        best = defaultdict(int)
        ans = 0

        for num in nums:
            best[num + 1] = best[num] + 1
            best[num] = best[num - 1] + 1
            ans = max(ans, best[num + 1], best[num])

        return ans

        