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

