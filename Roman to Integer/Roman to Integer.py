class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        previous = 0
        for char in reversed(s):
            current = roman[char]
            if current >= previous:
                total += current
            else:
                total -= current
            previous = current
        return total

# Test the solution
solution = Solution()

# Test cases
test_cases = ["III", "LVIII", "MCMXCIV"]

for case in test_cases:
    result = solution.romanToInt(case)
    print(f"Roman: {case}, Integer: {result}")
