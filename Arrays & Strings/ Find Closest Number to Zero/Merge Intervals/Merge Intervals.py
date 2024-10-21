class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        # Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result

# Test case
if __name__ == "__main__":
    sol = Solution()
    
    # Test case: [[1,3],[2,6],[8,10],[15,18]]
    test_intervals = [[1,3],[2,6],[8,10],[15,18]]
    
    print("Input intervals:", test_intervals)
    merged_intervals = sol.merge(test_intervals)
    print("Merged intervals:", merged_intervals)