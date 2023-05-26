class Solution:
    # Given n friends who play a game, return the list of losers (in ascending order)
    # when the game completes. 
    # 
    # The game is played by starting with the first player who throws
    # a ball to a the player that is k players away in clockwise order. Next,
    # the ball is thrown to the player 2 * k players away, and so on. 
    #
    # The game ends when a player gets the ball twice.
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # use a list to track the n players and whether they've gotten the ball
        # before index 0 represents player n, index 1 represents player 1.
        # False value means player hasn't gotten ball yet.
        players = [False] * n

        # Initialize player with ball to 1. Mod by n to handle case where
        # n == 1, in which case, index for player is 0
        playerWithBall = 1 % n
        
        # simulate rounds of the game and track players who've gotten 
        # the ball using the players list.
        roundNum = 1
        while True:
            # Check for game end condition -- whether current player with ball has 
            # gotten the ball before. If so, exit loop
            if players[playerWithBall]:
                break

            # Update player with ball's state
            players[playerWithBall] = True

            # Identify next player to get the ball. Note that index 0 containing
            # state for player n works well with how the mod operator works
            playerWithBall = (playerWithBall + (roundNum * k)) % n
            roundNum += 1
            
        # Create the list of lowers in ascending order to return. 
        sortedLosers = []
        for player, wasBallHolder in enumerate(players):
            # skip index 0 since it's actually player n
            if player == 0:
                continue

            if not wasBallHolder:
                sortedLosers.append(player)
        
        # process player n
        if not players[0]:
            sortedLosers.append(n)
        
        return sortedLosers
