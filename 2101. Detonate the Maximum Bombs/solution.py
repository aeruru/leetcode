class Solution:
    # Given a list of bombs, return the maximum number of bombs that
    # will detonate as part of a chain reaction by just detonating one
    # initial bomb. Each bomb is defined by a list of 3 
    # ints representing the x and y coordinates of the bomb and the 
    # radius affected by detonating the bomb. If the location of a
    # bomb is inside the circular region of a bomb detonation, it
    # will also detonate.
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Convert list of bombs into a directed graph where
        # an edge exists from bomb1 to bomb2 if detonating bomb1
        # would detonate bomb2 because the latter is within range
        # of bomb1's blast.

        # The graph is represented as a list of lists of bomb indices
        # that is within range of the bomb and will be detonated by
        # detonating the current bomb.
        graph = []
        for i in range(len(bombs)):
            graph.append([])

        # Iterate through every pair of bombs where order doesn't
        # matter because we consider edges going both ways for a pair
        # of bombs. So bomb1, bomb2 is the same as bomb2, bomb1
        for i in range(len(bombs)):
            (x1, y1, r1) = bombs[i]

            for j in range(i + 1, len(bombs)):
                (x2, y2, r2) = bombs[j]
                
                # For any two bombs, use the pythagorean theorem to
                # determine the square of the distance between their
                # locations.
                distanceSquared = ((x1 - x2)**2) + ((y1 - y2)**2)
                
                # Check distance squared against both bomb's ranges to 
                # determine whether bomb_i and bomb_j should have edges
                # to one another.
                if distanceSquared <= (r1 * r1):
                    graph[i].append(j)

                if distanceSquared <= (r2 * r2):
                    graph[j].append(i)

        
        # Track max bombs detonated for any initial bomb
        maxBombsDetonated = 0        

        # For each bomb, do a depth first search traversal to count the
        # total number of bombs that can be reached.
        for initialBombIndex in range(len(bombs)):
            # use a list to booleans to track visited state of the bombs
            visited = [False] * len(bombs)
            
            # Use a stack with int entries that represent the index 
            # of the bomb in the graph. Initialize with current bomb index
            # and mark that bomb as being visited. Initialize bombs detonated
            # counter to 1.
            stack = [initialBombIndex]
            visited[initialBombIndex] = True
            numBombsDetonated = 1

            # while the stack has more entries to process
            while stack:
                # Pop off the last entry to process
                bombIndex = stack.pop()

                # Add all of the bombs that this bomb can detonate that 
                # aren't currently visited (aka detonated already)
                for affectedBomb in graph[bombIndex]:
                    if not visited[affectedBomb]:
                        stack.append(affectedBomb)
                        numBombsDetonated += 1
                        visited[affectedBomb] = True

            # Once stack is empty and we've detonated as many bombs as
            # possible, update maxBombsDetonated
            if numBombsDetonated > maxBombsDetonated:
                maxBombsDetonated = numBombsDetonated

            # Minor optimization to return if max path length is equal
            # to the number of nodes which would mean every bomb was
            # detonated.
            if maxBombsDetonated == len(bombs):
                return maxBombsDetonated

        # Return max path length
        return maxBombsDetonated
