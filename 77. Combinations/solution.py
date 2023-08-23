class Solution:
    # Given two ints, n and k, return all possible combinations of 
    # length k consisting of numbers from 1 to n. The list of
    # possible combinations can be returned in any order.
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combineDFS(n, k)

    # Iterative solution similar to a Depth First Search traversal
    # using a stack
    def combineDFS(self, n: int, k: int) -> List[List[int]]:
        # List to hold the set of possible combinations to return
        combinations = []

        # We will implement an iterative DFS solution using a stack.
        # Each entry in the stack consists of two parts:
        #     1. The combination so far as a list, which we call committed choices
        #     2. The starting range of numbers up to and including n that
        #        remains to be used in a combination, we we call start range
        # The stack starts with an entry which has an empty combination and
        # a start range of 1 since the numbers 1 to n are still available to use.
        stack = [([],1)]
        
        # Loop while there are entries left in the stack to process
        while stack:
            # Take the most recent entry in the stack to process
            (committedChoices, startRange) = stack.pop()

            # calculate the number of choices left to make
            remainingChoices = k - len(committedChoices)
            # For each of numbers in the range that we can choose from,
            # create a entry in the stack to explore
            for newChoice in range(startRange, (n + 1) - (remainingChoices - 1)):
                # We have to create a copy of committed choices or else
                # on the next iteration, committedChoices will contain
                # additional entries added during this iteration of the loop.
                newCommittedChoices = committedChoices.copy()

                # Add newChoice to our new list of committed choices
                newCommittedChoices.append(newChoice)
                
                # If we've made all of our k choices, add this now complete
                # combination to our list of all possible combinations
                if len(newCommittedChoices) == k:
                    combinations.append(newCommittedChoices)
                    continue
                
                # There are more choices to make so add a new DFS node
                # to our stack for the subproblem where we have one less
                # number to choose from for the remaining choices
                stack.append((newCommittedChoices, newChoice + 1))
        
        # return all the combinations we've generated
        return combinations

    # Recursive version where the base case returns the set of possible
    # combinations for the initial conditions.
    def combineRecursive(self, n: int, k: int) -> List[List[int]]:

        # Recursive helper function that takes in the choices that have already 
        # been made (curChoices), the first number that can still be considered 
        # for choices and the number of remaining choices to be made. This 
        # function returns a list of complete combinations found so far.
        def combineHelper(curChoices: List[int], startRange: int, numChoices: int) -> List[List[int]]:
            
            # List used to collect the set of possible combinations
            results = []

            # Iterate starting from startRange, which is the first number
            # that we should consider without creating duplicate combinations, 
            # up until there are enough numbers left to make the remaining choices. 
            # n+1 is to include the number n in the range call. numChoices-1 is 
            # the number of choices we will need to make after the choice we make
            # in this call of the function. 
            for i in range(startRange, (n + 1) - (numChoices - 1)):
                # We need to create a copy of curChoices or else the next iteration 
                # of this loop will have i and other elements added from executing
                # this iteration.
                newCurChoices = curChoices.copy()

                # Choose i and add it to our current list of choices.
                newCurChoices.append(i)

                # While we have more than 1 choice left to make, call this recursive
                # function with the list of choices we've made so far, a smaller
                # range of numbers that we can make our remaining choices with, and 
                # one fewer choice we need to make. The result will be a list of
                # combinations that we add to results. 
                #
                # Note that we don't need to make choices with numbers smaller than i 
                # because all combinations with smaller numbers have already been 
                # covered in previous iterations of this loop or in previous calls of
                # this recursive method.
                if numChoices > 1:
                    results.extend(combineHelper(newCurChoices, i + 1, numChoices - 1))
                    continue

                # We only get here if numChoices is 1. In that case, we've just made our 1
                # choice (i) and added it to newCurChoices so that it is now a complete 
                # combination. Add it to results before continuing the loop.
                results.append(newCurChoices)

            # Return all the combinations we've completed so far
            return results

        return combineHelper([], 1, k)

    # Psuedocode for the approach to recursion from Cody's solution!
    def combineRecursive2(self, n: int, k: int) -> List[List[int]]:
        # Define an inline recursive helper method inside of combine that takes 
        # two args:
        #     1. startRange - the start of the range of numbers up to n left to
        #        make choices from (note that the inline function has access to n)
        #     2. numChoices - number of choices that still need to be made
        # The helper method returns a list of all possible combinations for the
        # subproblem defined by startRange, n and numChoices
        def combineHelper(startRange: int, numChoices: int) -> List[List[int]]:
            # For the base case, if there are zero choices left to make, then
            # the only possible combination is an empty one. Return a list with
            # the empty combination.

            # Declare results variable to collect all the possible combinations
    
            # Iterate through all elements from startRange to n while there are 
            # enough numbers remaining to make the remaining choices minus the 
            # choice we will make now.
    
                # Get all the possible combos for the subproblem where we have
                # one less choice to make and our range of numbers is one smaller.
                
                # For each of the possible combos returned above, add the current
                # number to create combos with size equal to numChoices. Note 
                # that it doesn't matter if you add the current number to the end
                # as LeetCode will accept any order. Then add the combos to results.

            # return results which will contain all the possible combos
            return [[]]
        
        # Call combineHelper with the initial arguments to choose k number from the
        # range 1 to n. Return the results.
        return [[]]
