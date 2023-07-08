class Solution:
    # Given a 0-indexed integer array nums, find the total 
    # number of beautiful pairs in nums. A beautiful pair
    # means:
    # 1. Two numbers in nums
    # 2. The first digit of the number at a lower index and the
    #   last digit of the number at the higher index are coprime.
    # Two numbers are coprime if their greatest common divisor
    # is 1.
    def countBeautifulPairs(self, nums: List[int]) -> int:
        # Find all pairs of numbers in nums and get first digit
        # of the number at the lower index and the last digit 
        # of the higer index
        countBeautifulPairs = 0

        # Do a double iteration to get pairs of numbers.
        # The first index can only go up to len(nums) - 2 to leave
        # room for the second number
        for i in range(len(nums) - 1):
            # convert first number of the pair to a string to
            # get the first digit and then convert that back to an int
            firstNumberDigit = int(str(nums[i])[0])

            for j in range (i + 1, len(nums)):
                # use mod to get the last digit as an int of the second number
                secondNumberDigit = nums[j] % 10
                
                if self.isCoprime(firstNumberDigit, secondNumberDigit):
                    countBeautifulPairs += 1
    
        return countBeautifulPairs

    # Returns whether two numbers are coprime, meaning their GCD is 1
    def isCoprime(self, num1: int, num2: int) -> int:
        # Check numbers starting from 2 up to the smaller number.
        # If any number divides both evenly, these numbers are not coprime
        for divisor in range(2, min(num1, num2) + 1):
            if num1 % divisor == 0 and num2 % divisor == 0:
                return False

        # No divisor found for both numbers so they are coprime
        return True
