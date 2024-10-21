class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Find the shortest string in the list
        shortest = min(strs, key=len)
        
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]
        
        return shortest
