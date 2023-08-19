class Solution:
    # Given a list of unique integers called nums, return the list of all possible
    # permutations of the elements of nums.
    def permute(self, nums: List[int]) -> List[List[int]]:
        # base case is if there is just one item in nums. Then just return
        # that as the only possible permutation in a list.
        if len(nums) == 1:
            return [nums]

        # Variable to store all permutations for this call of permute
        results = []

        # iterate through each item in nums to find all permutations that start
        # with that item.
        for i in range(len(nums)):
            # create a copy of nums with the item at the current index
            # removed
            newCandidates = nums.copy()
            newChoice = newCandidates.pop(i)

            # recursively call this function with a subproblem containing
            # one fewer element in nums
            permutations = self.permute(newCandidates)

            # Iterate through the permutations returned from the subproblem.
            # Add the current newChoice to the permutations. 
            for permutation in permutations:
                permutation.append(newChoice)
            
            # Add the new permutations to results
            results.extend(permutations)
        
        # return all permutations found in this call of permute
        return results
