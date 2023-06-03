class Solution:
    # Given a string of uppercase English letters, repeatedly remove
    # any instances of "AB" or "CD" from the string until no more instances
    # exist. Return the length of the resulting string.
    def minLength(self, s: str) -> int:

        # minLength will keep track of the length of the string as we remove
        # the two sequences from s
        minLength = len(s)

        # Iterate through s using a stack to track characters that are part
        # of the two special substrings. A key insight of this implementation
        # is that no AB or CD sequences are possible around a letter that is 
        # not A, B, C or D so we can clear our tracking in that case.
        stack = []

        for letter in s:
            # If letter is one of the 4 special characters, push it on the stack. 
            if letter == 'A' or letter == 'B' or letter == 'C' or letter == 'D':
                stack.append(letter)
            # Otherwise, we can clear our tracking because no special sequences
            # can be formed with letters that came before this "non-special" 
            # character
            else:
                stack.clear()

            # If the stack has at least 2 elements, check if last two elements
            # form either of the sequences and delete them.
            if len(stack) >= 2:
                if (stack[-1] == 'B' and stack[-2] == 'A') or (stack[-1] == 'D' and stack[-2] == 'C'):
                    stack.pop()
                    stack.pop()
                    minLength -= 2
        
        # With all substrings deleted, length of s is now the minimum string.
        return minLength
