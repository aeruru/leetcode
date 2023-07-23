class Solution:
    # Given an initial list of locations for marbles, represented as integers, and two 
    # other lists representing move operations, return the sorted list of integer locations
    # where there are still marbles after applying all move operations.
    
    # Move operation i takes all the marbles from location moveFrom[i] and puts them at
    # moveTo[i]. Move operations will be applied sequentially. Each moveFrom operation
    # is guaranteed to specify an index where there are marbles.
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        # Use a set to represent occupied positions. This is because we only need to
        # represent whether a position is occupied or not and do not need to track
        # the number of marbles at a particular position.
        occupiedPositions = set(nums)

        # Iterate through move operations to apply them
        for i in range(len(moveFrom)):
            # Since moveFrom removes all marbles from that location, we can delete the
            # location from our set
            occupiedPositions.remove(moveFrom[i])

            # Check if the position we're moving the marbles too is already marked
            # as occupied and only call 'add' if that's not the case. (This is a minor
            # perf optimization based on a small number of manual tests using 'Run'.)
            if moveTo[i] not in occupiedPositions:
                occupiedPositions.add(moveTo[i])

        # Use python's sorted function to sort the occupied positions in the set
        return sorted(occupiedPositions)
