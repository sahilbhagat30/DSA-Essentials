from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

def test_max_profit(prices: List[int], expected: int) -> None:
    sol = Solution()
    result = sol.maxProfit(prices)
    print(f"Prices: {prices}")
    print(f"Expected: {expected}, Got: {result}")
    assert result == expected, f"Test failed! Expected {expected}, but got {result}"
    print("Test passed!")
    print()

def main():
    # Test case 1: Standard case
    test_max_profit([7,1,5,3,6,4], 5)

    # Test case 2: Prices in ascending order
    test_max_profit([1,2,3,4,5], 4)

    # Test case 3: Prices in descending order
    test_max_profit([5,4,3,2,1], 0)

    # Test case 4: Empty list
    test_max_profit([], 0)

    # Test case 5: Single element
    test_max_profit([1], 0)

    # Test case 6: Two elements
    test_max_profit([1,2], 1)

    # Test case 7: More complex case
    test_max_profit([3,3,5,0,0,3,1,4], 4)

    print("All tests passed!")

if __name__ == "__main__":
    main()
