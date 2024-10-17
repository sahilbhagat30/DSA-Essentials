class Solution(object):
    def longestCommonPrefix(self, strs):
        match_index = 0
        match_string = 0
        for i in range(len(min(strs))):
            for j in strs:
                if strs[j][i] == strs[strs.index(min(strs))][i]:
                    match_string += 1
                else:
                    break
            if match_string == len(strs):
                match_index += 1
        return strs[0][:match_index] if match_index > 0 else ""
