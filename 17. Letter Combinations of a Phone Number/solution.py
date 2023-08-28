class Solution:
    # Mapping from digits 2-9 to letters a-z based on the system used by phones
    digitToLettersMap = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    # Given a string of digits from 2-9 inclusive, return all letter combinations
    # that the numbers can represent. Numbers map to a set 3 letters based on
    # the system used by phones.
    def letterCombinations(self, digits: str) -> List[str]:
        # This implementation will focus on low memory usage by
        # defining a buffer that will be reused throughout the algorithm
        letterComboBuffer = [' '] * len(digits)

        # List that holds all the possible letter combinations
        combinations = []

        # Define a recursive helper method that solves the subproblem. This
        # method will use letterComboBuffer to construct letter
        # combinations and digitIndex to determine which digit to process.
        def combinationHelper(digitIndex: int):
            digit = digits[digitIndex]
 
            # Loop through the possible letters for the current digit
            for letter in Solution.digitToLettersMap[digit]:
                letterComboBuffer[digitIndex] = letter

                # If this is the last digit to process, convert the letter 
                # combo buffer to a string and add it to combinations. No more 
                # recursion is needed.
                if digitIndex == len(digits) - 1:
                    combinations.append("".join(letterComboBuffer))
                    continue
                
                # Otherwise, keep calling combination helper on the next digit
                combinationHelper(digitIndex + 1)

            return None

        # If there are any digits, call the recurive function
        if digits:
            combinationHelper(0)

        # Return all the letter combinations found
        return combinations
