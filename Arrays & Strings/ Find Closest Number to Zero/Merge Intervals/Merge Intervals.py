class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        
        print(intervals[0])

        # # Sort intervals based on start time
        # intervals.sort(key=lambda x: x[0])
        
        # result = [intervals[0]]

        # for interval in intervals[1:]:
        #     if interval[0] <= result[-1][1]:
        #         result[-1][1] = max(result[-1][1], interval[1])
        #     else:
        #         result.append(interval)

        # return result

# Test case
if __name__ == "__main__":
    sol = Solution()
    
    # Test case: [[1,3],[2,6],[8,10],[15,18]]
    test_intervals = [[1,3],[2,6],[8,10],[15,18]]
    
    print("Input intervals:", test_intervals)
    merged_intervals = sol.merge(test_intervals)
    # print("Merged intervals:", merged_intervals)

    # # Expected output: [[1,6],[8,10],[15,18]]
    # print("Expected output: [[1,6],[8,10],[15,18]]")

    # # Verify if the output matches the expected result
    # expected_output = [[1,6],[8,10],[15,18]]
    # if merged_intervals == expected_output:
    #     print("Test case passed!")
    # else:
    #     print("Test case failed.")