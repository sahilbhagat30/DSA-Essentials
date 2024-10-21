# Longest Common Prefix

## Problem Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Example 1

**Input:** strs = ["flower","flow","flight"]
**Output:** "fl"

## Example 2

**Input:** strs = ["dog","racecar","car"]
**Output:** ""
**Explanation:** There is no common prefix among the input strings.

## Constraints

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.

## Approach

To solve this problem, we can use the following approach:

1. If the input array is empty, return an empty string.
2. Take the first string in the array as the initial prefix.
3. Iterate through the remaining strings:
   - Compare the current prefix with each string.
   - Shorten the prefix until it matches the beginning of the current string.
   - If the prefix becomes empty at any point, return an empty string.
4. Return the final prefix.

## Solution

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
```

## Complexity Analysis

- Time Complexity: O(S), where S is the sum of all characters in all strings. In the worst case, we might need to compare all characters of all strings.
- Space Complexity: O(1), as we only use a constant amount of extra space.

## Alternative Approach: Vertical Scanning

Another approach is to scan the strings vertically, comparing characters at the same index for all strings:

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        
        return strs[0]
```

This approach can be more efficient if there are many strings with a small common prefix.

## Related Topics

- String
- Trie (for more advanced solutions)

## LeetCode Link

[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)
