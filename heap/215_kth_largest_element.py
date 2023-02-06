import heapq

class Solution:
    def findKthLargest(self, nums, k):
        largest = []
        for num in nums:
            heapq.heappush(largest, num)
            if len(largest) > k:
                heapq.heappop(largest)
        return largest[0]

solver = Solution()
# Example 1
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(solver.findKthLargest(nums, k))  # Output: 5

# Example 2
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(solver.findKthLargest(nums, k))  # Output: 4
