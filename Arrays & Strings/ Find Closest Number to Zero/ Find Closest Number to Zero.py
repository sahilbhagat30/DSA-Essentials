class Solution(object):
    def findClosestNumber(self, nums):
        closest = nums[0]

        for x in nums:
            if abs(x) < abs(closest):
                closest = x

        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest

# Test cases
test_cases = [
    [-4, -2, 1, 4, 8],
    [2, -1, 1],
    [5, 10, 0, 3, -1],
    [-100000, 100000],
    [-1, 1, 2, -2, 3, -3]
]

# Create an instance of the Solution class
solution = Solution()

# Run test cases and print results
for i, nums in enumerate(test_cases, 1):
    result = solution.findClosestNumber(nums)
    print(f"Test case {i}:")
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print()
