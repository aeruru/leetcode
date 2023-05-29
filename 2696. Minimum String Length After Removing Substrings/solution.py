class Solution:
    # Given a string of uppercase English letters, repeatedly remove
    # any instances of "AB" or "CD" from the string until no more instances
    # exist. Return the length of the resulting string.
    def minLength(self, s: str) -> int:

        # Convert from an immutable string to a list so we can delete items
        # from it
        listS = list(s)

        # Iterate through s using the index so that modification of the list
        # is safe. We don't need to look at the last letter since
        # we look forward when we see an "A" or "C".
        i = 0
        while i < len(listS) - 1:

            letter = listS[i]
            nextLetter = listS[i+1]
            doDeletes = False

            # Check for "AB" and "CD" sequences and flag them for deletion
            match letter:
                case 'A': 
                    if nextLetter == 'B':
                        doDeletes = True
                case 'C':
                    if nextLetter == 'D':
                        doDeletes = True
            
            # print(f"remaining list: {listS[i:]}")

            # Pop the current letter and next off the list since both
            # "AB" and "CD" are length two sequences.
            if doDeletes:
                listS.pop(i)
                listS.pop(i)
                # If possible, back index up by one and look to see if the 
                # letters surrounding the deleted ones form one of the sequences
                # Example: CABD -> After removing AB, a CD sequence is formed
                if i > 0:
                    i -= 1

                # print(f"After delete, i = {i} and list = {listS}")
                continue

            # If we didn't find a sequence, increment index and continue looking 
            i += 1

        # With all substrings deleted, length of s is now the minimum string.
        return len(listS)
