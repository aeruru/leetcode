class Solution:
    # Given an bit array, determine whether a bit array exists such that doing
    # a neighboring bitwise xor transformation yields the input array, derived. 
    #
    # The bitwise xor operation xors the value in a bit array with the value to
    # the right, wrapping around at the end
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        # Start by populating possible original arrays with 0 and 1
        possibilities = [[0], [1]]
        
        # for each value in derived, create possible bit arrays that would work
        # after doing a bitwise xor operation
        for i, curBit in enumerate(derived):
            for p in possibilities:
                # if derived value is the same as the current bit value in original,
                # then the neighboring value has to be a 0:
                #    derived_i = 0   original_i = 0  => original_i+1 = 0
                #    derived_i = 1   original_i = 1  => original_i+1 = 0
                # Similarly if derived value is not equal with the current original bit
                # value, then the neigboring value has to be a 1:
                #    derived_i = 0   original_i = 1  => original_i+1 = 1
                #    derived_i = 1   original_i = 0  => original_i+1 = 1
                if p[-1] == curBit:
                    p.append(0)
                else:
                    p.append(1)

        # Note that our possibilities array now has one element more than derived
        # because derived_n-1 generated original_n. Since derived_n-1 is supposed to
        # be original_n-1 xor original_0, we must check if original_n is equal to
        # original_0 for either possibilities. If not, then there are no possible
        # original arrays.
        return possibilities[0][0] == possibilities[0][-1] or possibilities[1][0] == possibilities[1][-1]
