class Solution:
    def mergeAlternately(self, word1, word2):
        result = ""
        i= 0
        n1 = len(word1)
        n2 = len(word2)
        while i < n1 and i < n2:
            result+=word1[i]
            result+=word2[i]
            i += 1
        if i == n1:
            return result+word2[i:]
        else:
            return result+word1[i:]
    
    # Test cases
test_cases = [
    ["abc","pqr"],
    ["ab","pqrs"],
    ["abcd","pq"]
    # ... other test cases ...
]

# Create an instance of the Solution class
solution = Solution()

# Run test cases and print results
for i, words in enumerate(test_cases, 1):
    result = solution.mergeAlternately( words[0], words[1])
    print(f"Test case {i}:")
    print(f"Input: Word1: {words[0]}, Word2: {words[1]}")
    print(f"Output: {result}")
    print()
