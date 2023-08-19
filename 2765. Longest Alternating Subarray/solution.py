class Solution:
    # Given a array of integers, nums, find the longest alternating
    # subarray within nums. A subarray is a contiguous, non-empty 
    # sequence of elements in nums that meet the following criteria:
    #   - The subarray is longer than 1 element
    #   - The subarray starts with an integer n and the next element
    #     must be n+1
    #   - From then on, the difference between each successive element
    #     of the subarray alternates between -1 and 1.
    # Return -1 if there is no such subarray
    def alternatingSubarray(self, nums: List[int]) -> int:
        # Track max and current subarray length
        maxLength = 0
        curLength = 0

        # Track whether the difference between successive elements
        # should be 1 or -1. In this problem, the subarray must start
        # with a difference of 1
        expectedDiff = 1

        # Iterate through nums to look for subarrays. Use index
        # based iteration so we can look at two elements.
        i = 0
        while i < len(nums) - 1:

            # Check if the current element and next element have a 
            # difference that meets the conditions. 
            if nums[i+1] - nums[i] != expectedDiff:
                # They don't meet the conditions. Check if we need
                # to update max subarray length before reseting the
                # current length counter.
                maxLength = max(maxLength, curLength)
                curLength = 0
                
                # Set the expected difference back to 1 for the start
                # of a new subarray. 
                expectedDiff = 1

                # If the difference is 1, continue iterating but
                # don't increment i because this is the start of a 
                # new subarray. Otherwise, increment i and continue
                # looking for a subarray that meets the conditions.
                if nums[i+1] - nums[i] != 1:
                    i += 1

                continue
            
            # The current element and the next element do meet the
            # conditions to continue the subarray. Increment the current
            # subarray length. Switch expected diff to -1 if it is 
            # currently 1 or vice versa.
            curLength += 1
            expectedDiff *= -1

            # Increment i to keep looking
            i += 1

        # Check one last time if we need to update max length
        maxLength = max(maxLength, curLength)

        # Return -1 if we never found a subarray
        if maxLength == 0:
            return -1

        # Return maxLength + 1 since we initialize curLength to 0 but
        # the first time we identify a subarray that means it now has
        # length two and not 1
        return maxLength + 1
