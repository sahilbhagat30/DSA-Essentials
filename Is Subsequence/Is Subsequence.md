# Is Subsequence

## Problem Description

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

## Examples

### Example 1:

**Input:** s = "abc", t = "ahbgdc"
**Output:** true

### Example 2:

**Input:** s = "axc", t = "ahbgdc"
**Output:** false

## Constraints:

- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters.

## Follow up:

Suppose there are lots of incoming `s`, say `s1, s2, ..., sk` where `k >= 109`, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?

## Approach

To solve this problem, we can use a two-pointer approach:
1. Initialize two pointers, one for `s` and one for `t`.
2. Iterate through `t`, and whenever we find a character that matches the current character in `s`, move the pointer for `s`.
3. If we've gone through all characters in `s`, it's a subsequence.

## Solution

Here's a Python solution to the problem:

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


```

## Simple Solution

This solution uses a two-pointer approach and is efficient for a single query:

```python
class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True
        if len(s) > len(t):
            return False
        i = 0
        for l in t:
            if l == s[i]:
                i += 1
                if len(s) == i:
                    return True
        return False
```

### Complexity Analysis:
- Time Complexity: O(n), where n is the length of t.
- Space Complexity: O(1).

## Optimized Solution for Multiple Queries

This solution preprocesses string `t` to handle multiple queries efficiently:

```python
from collections import defaultdict
import bisect

class Solution(object):
    def __init__(self):
        self.char_indices = defaultdict(list)

    def preprocess(self, t):
        for i, char in enumerate(t):
            self.char_indices[char].append(i)

    def isSubsequence(self, s, t):
        if not self.char_indices:
            self.preprocess(t)

        curr_index = -1
        for char in s:
            if char not in self.char_indices:
                return False
            indices = self.char_indices[char]
            j = bisect.bisect_right(indices, curr_index)
            if j == len(indices):
                return False
            curr_index = indices[j]
        return True
```

### Complexity Analysis:
- Preprocessing Time: O(n), where n is the length of t.
- Query Time: O(m log n), where m is the length of s.
- Space Complexity: O(n) for storing the preprocessed data.

## Usage

```python
# Create an instance of the Solution class
solution = Solution()

# Test cases
test_cases = [
    ("abc", "ahbgdc"),
    ("axc", "ahbgdc"),
    ("", "ahbgdc"),
    ("acb", "ahbgdc"),
    ("aaaaaa", "bbaaaa")
]

# Run test cases and print results
for i, (s, t) in enumerate(test_cases, 1):
    result = solution.isSubsequence(s, t)
    print(f"Test case {i}:")
    print(f"s: {s}")
    print(f"t: {t}")
    print(f"Is subsequence: {result}")
    print()
```

This optimized solution is particularly useful for the follow-up question where you need to check multiple strings against the same `t`. After preprocessing `t` once, each subsequent check becomes more efficient.
