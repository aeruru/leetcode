class Solution:
    # Given a grid of 0s and 1s, find the length of the shortest path
    # from the top left cell to the bottom right cell that only goes through
    # cells containing a 0. Each cell is connected to the 8 cells around it
    # that either share an edge or a corner. If no path is found, return -1.
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Check that top left and bottom right cells contain 0s. Otherwise no clear
        # path can exist, so return -1
        gridHeight = len(grid)
        gridWidth = len(grid[0])
        
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        # Use BFS to find the shortest path so keep track of nodes
        # to visit in a queue. Each entry is a tuple of the col and row index of
        # the cell to visit. Initialize queue with top left cell.
        queue = [(0,0)]
        
        # Set top left cell value to -1 to indicate it has been visited.
        grid[0][0] = -1

        # Loop while there are more nodes to visit. Each loop here represents a round.
        # Start roundNum at 1 since a grid of 1x1 will have a path length of 1.
        roundNum = 1
        while queue:

            # Go through each of the nodes currently in the queue which will be all
            # the nodes we process in this round
            numCurrentRoundCells = len(queue)
            while numCurrentRoundCells > 0:

                # pop next cell from front of queue to process. It is a tuple of the
                # row index and col index of the cell.
                (row, col) = queue.pop(0)
                # print(f"Processing ({row}, {col})")

                # decrement loop counter after popping entry off of the queue
                numCurrentRoundCells -= 1

                # If we've reached the bottom right cell, we've found our shortest path
                # which should have a length that is the same as the number of rounds
                # of the BFS traversal.
                if row == gridHeight - 1 and col == gridWidth - 1:
                    return roundNum

                # Loop through the 8 cells surrounding the current cell and 
                # append any that have a value of 0 to the queue.
                for rowOffset in [-1, 0, 1]:
                    adjacentRow = row + rowOffset
                    
                    # check for invalid row indices
                    if adjacentRow < 0 or adjacentRow >= gridHeight:
                        continue
                    
                    for colOffset in [-1, 0, 1]:
                        adjacentCol = col + colOffset
                        
                        # check for invalid col indexes
                        if adjacentCol < 0 or adjacentCol >= gridWidth:
                            continue

                        # Check if value of cell is 0. Note that we don't have to
                        # check for the case where rowOffset and colOffset are both
                        # 0 which points to the current cell that is being processed
                        # because when that cell was added to the queue, its value was
                        # set to -1 to indicate it's been visited. That means it will
                        # not be appended because this we only append cells with value 0.
                        # print(f"Checking adjacent cell ({adjacentRow}, {adjacentCol})")
                        if grid[adjacentRow][adjacentCol] == 0:
                            # Append cell with value 0 to queue and also mark it with -1
                            # to indicate it has been visited
                            queue.append((adjacentRow, adjacentCol))
                            grid[adjacentRow][adjacentCol] = -1
                            # print(f"Adding adjacent cell ({adjacentRow}, {adjacentCol}) to queue")

            # Increment the number of rounds in the outer loop
            roundNum += 1

        # No path was found so return -1
        return -1
