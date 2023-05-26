class Solution:
    # Given a bit array, determine whether a bit array exists such that doing
    # a neighboring bitwise xor transformation yields the input array, derived. 
    #
    # The bitwise xor operation xors the value in a bit array with the value to
    # the right, wrapping around at the end
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        # For each value in derived, see if a possible bit array would work starting
        # for a value of 0 at index 0 of original. Since starting from bit 1 would just
        # result in an inverse array, if there is no possible original bit array when we
        # assume original starts with a 0, there would be no possible original bit array
        # if we started with 1 at index 0 of original.
        original = [0]
        for i, curBit in enumerate(derived):
            # if derived value is the same as the current bit value in original,
            # then the neighboring value has to be a 0:
            #    derived_i = 0   original_i = 0  => original_i+1 = 0
            #    derived_i = 1   original_i = 1  => original_i+1 = 0
            # Similarly if derived value is not equal with the current original bit
            # value, then the neigboring value has to be a 1:
            #    derived_i = 0   original_i = 1  => original_i+1 = 1
            #    derived_i = 1   original_i = 0  => original_i+1 = 1
            if original[-1] == curBit:
                original.append(0)
            else:
                original.append(1)

        # Note that our original array now has one element more than derived
        # because derived_n-1 generated original_n. Since derived_n-1 is supposed to
        # be original_n-1 xor original_0, we must check if original_n is equal to
        # original_0. If not, then there are no possible
        # original arrays.
        return original[0] == original[-1]
