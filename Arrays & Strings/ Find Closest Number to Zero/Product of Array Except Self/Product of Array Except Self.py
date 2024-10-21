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

# Example usage and tests
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1, 2, 3, 4]
    print("Input:", nums1)
    print("Output:", sol.productExceptSelf(nums1))
    print("Expected: [24, 12, 8, 6]")
    print()
    
    # Example 2
    nums2 = [-1, 1, 0, -3, 3]
    print("Input:", nums2)
    print("Output:", sol.productExceptSelf(nums2))
    print("Expected: [0, 0, 9, 0, 0]")
    print()
    
    # Additional test cases
    # Test case 3: Array with ones
    nums3 = [1, 1, 1, 1]
    print("Input:", nums3)
    print("Output:", sol.productExceptSelf(nums3))
    print("Expected: [1, 1, 1, 1]")
    print()
    
    # Test case 4: Array with zeros
    nums4 = [0, 1, 2, 0, 3]
    print("Input:", nums4)
    print("Output:", sol.productExceptSelf(nums4))
    print("Expected: [0, 0, 0, 0, 0]")
    print()
    
    # Test case 5: Larger array
    nums5 = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Input:", nums5)
    print("Output:", sol.productExceptSelf(nums5))
    print("Expected: [40320, 20160, 13440, 10080, 8064, 6720, 5760, 5040]")
