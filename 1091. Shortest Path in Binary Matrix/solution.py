class Solution:
    # Given a grid of 0s and 1s, find the length of the shortest path
    # from the top left cell to the bottom right cell that only goes through
    # cells containing a 0. Each cell is connected to the 8 cells around it
    # that either share an edge or a corner. If no path is found, return -1.
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Use BFS to find the shortest path so keep track of nodes
        # to visit in a queue. Each entry is a tuple of the col and row index of
        # the cell to visit.

        # Use a grid of bool to track if nodes have been visited.

        # Loop while there are more nodes to visit. Each loop here represents a round.

            # Go through each of the nodes currently in the queue which will be all
            # the nodes we process in this round

                # Add any connected cells to the current cell that hasn't been visited

                # If we've reached the bottom right cell, we've found our shortest path
                # which should have a length that is the same as the number of rounds
                # of the BFS traversal.
            
            # Increment the # of rounds

        # No path was found so return -1
