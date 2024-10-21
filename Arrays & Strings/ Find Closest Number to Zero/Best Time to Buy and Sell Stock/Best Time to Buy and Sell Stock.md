# Best Time to Buy and Sell Stock

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Example 1

**Input:** prices = [7,1,5,3,6,4]
**Output:** 5
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

## Example 2

**Input:** prices = [7,6,4,3,1]
**Output:** 0
**Explanation:** In this case, no transactions are done and the max profit = 0.

## Constraints

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

## Approach

To solve this problem, we can use a single pass through the array, keeping track of the minimum price seen so far and the maximum profit that can be achieved. Here's the algorithm:

1. Initialize variables:
   - `min_price` to keep track of the minimum price seen so far
   - `max_profit` to store the maximum profit that can be achieved
2. Iterate through the prices array:
   - Update `min_price` if the current price is lower
   - Calculate the potential profit by subtracting `min_price` from the current price
   - Update `max_profit` if the potential profit is higher
3. Return `max_profit`

## Solution

```python
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

        

```
## Complexity Analysis

- Time Complexity: O(n), where n is the number of prices in the input array. We make a single pass through the array.
- Space Complexity: O(1), as we only use a constant amount of extra space.

## Related Topics

- Array
- Dynamic Programming

## LeetCode Link

[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
