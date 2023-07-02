class Solution:
    # Given a string w/ only lowercase English letters, turn the string into a 
    # palindrome by making the smallest number of edits to the string and
    # creating the lexicographically smallest pallindrome. Lexicographically smallest
    # just means alphabetically smaller when each letter is compared from left to
    # right.Return the pallindrome.
    def makeSmallestPalindrome(self, s: str) -> str:
        
        # convert immutable string s into a list so we can modify in place
        listS = list(s)
        
        # Iterate through the first half of the string, not including the middle character
        # if the string has an odd length
        for i in range(len(listS)//2):
            # Use negative indices to find the corresponding character from the end of the
            # string. The letter at index 0 should be compared with the letter at index -1,
            # the letter at index 1 compared with the letter at index -2, and so on.
            # Since we want the alphabetically smallest pallindrome string, compare the
            # letters and use the smaller one to turn the string into a pallindrome.
            if listS[i] < listS[-(i + 1)]:
                listS[-(i + 1)] = listS[i]
            else:
                listS[i] = listS[-(i + 1)]
        
        # Use the join operator to create a string from the list of characters. The ''
        # infront specfies any delimiters between characters which we don't want in this
        # case.
        return ''.join(listS)
