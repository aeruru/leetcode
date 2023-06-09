class Solution:
    # Given a positive integer n, return the punishment number of n which
    # is determined by adding up the squares of any integer i that is 
    # between 1 and n (inclusive) and the following complicated condition:
    # The square of i can be partitioned into contiguous substrings so that
    # the sum of the integers values of the substrings is equal to i.
    def punishmentNumber(self, n: int) -> int:

        # For each integer between 1 and n inclusive...
        punishmentNum = 0
        for i in range(1,n+1):
            # call helper function to determine whether it meets criteria to be
            # included in punishment number.
            if Solution.canBePartitionedRecursive(i):
                # if criteria is met, add the square of i to punishment number
                punishmentNum += i * i

        return punishmentNum

    # Given an int i, return whether the string representation of i squared can
    # be partitioned into substrings such that the sum of the integer value
    # of the substrings equals i. This is an interative algorithm.
    def canBePartitionedIterative(i: int) -> bool:
        # TODO
        return False
    
    # Given an int i, return whether the string representation of i squared can
    # be partitioned into substrings such that the sum of the integer value
    # of the substrings equals i. This is a recursive algorithm.
    def canBePartitionedRecursive(i: int) -> bool:
        # convert square of i into a string
        s = str(i * i)
        # call helper method which takes i as a string and sets the 
        # target for the sum to be i.
        return Solution.canBePartitionedRecursiveHelper(s, target=i)

    # Given a string s and a integer target, return whether s can be
    # partitioned into substrings such that the sum of the integer value
    # of the substrings equals the target.
    def canBePartitionedRecursiveHelper(s: str, target:int) -> bool:
        # print(f"s={s}, target={target}")

        # convert s to an int
        i = int(s)
        
        # if s is equal to the target, then we've found a way to partition
        # the string to add up to the number we want
        if i == target:
            print(f"Partition found")
            return True

        # if i is a single digit, then there is no more recursion we can do.
        # since i is not the same as target, this attempt at partioning failed.
        if i < 10:
            return False
        
        # otherwise, loop through s and try partioning off the first x digits
        # until we find a partition that adds up to the target. If we find it
        # return True, otherwise return False.
        for x in range(1, len(s)):
            firstDigits = s[:x]
            firstDigitsAsInt = int(firstDigits)
            remainingDigits = s[x:]
            # recursively call helper with the remaining digits as a string and
            # with the target being the current target minus the integer value
            # of the first digits
            if Solution.canBePartitionedRecursiveHelper(s=remainingDigits, target=target - firstDigitsAsInt):
                return True

        # no partition that met target could be found so return False.
        return False
