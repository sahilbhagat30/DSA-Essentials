# Product of Array Except Self

## Problem Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Example 1

**Input:** nums = [1,2,3,4]
**Output:** [24,12,8,6]

## Example 2

**Input:** nums = [-1,1,0,-3,3]
**Output:** [0,0,9,0,0]

## Constraints

- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

## Follow up

Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

## Approach

To solve this problem efficiently without using division and in O(n) time, we can use a two-pass approach:

1. First pass: Calculate the product of all elements to the left of each element.
2. Second pass: Calculate the product of all elements to the right of each element and multiply it with the left product.

## Solution

```python
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        
        # Calculate left products
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # Calculate right products and combine
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result
```


## Complexity Analysis

- Time Complexity: O(n), where n is the length of the input array. We make two passes through the array.
- Space Complexity: O(1) extra space, not counting the output array. We only use a constant amount of extra space.

## Related Topics

- Array
- Prefix Sum

## LeetCode Link

[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)