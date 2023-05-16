from util import manhattanDistance
from game import Directions
import random
import util
from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and child states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(
            gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(
            len(scores)) if scores[index] == bestScore]
        # Pick randomly among the best
        chosenIndex = random.choice(bestIndices)

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        The evaluation function takes in the current and proposed child
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.
        """
        # Useful information you can extract from a GameState (pacman.py)
        childGameState = currentGameState.getPacmanNextState(action)
        newPos = childGameState.getPacmanPosition()
        newFood = childGameState.getFood()
        newGhostStates = childGameState.getGhostStates()
        newScaredTimes = [
            ghostState.scaredTimer for ghostState in newGhostStates]

        minGhostDistance = min(
            [manhattanDistance(newPos, state.getPosition()) for state in newGhostStates])

        scoreDiff = childGameState.getScore() - currentGameState.getScore()

        pos = currentGameState.getPacmanPosition()
        nearestFoodDistance = min([manhattanDistance(pos, food)
                                  for food in currentGameState.getFood().asList()])
        newFoodsDistances = [manhattanDistance(
            newPos, food) for food in newFood.asList()]
        newNearestFoodDistance = 0 if not newFoodsDistances else min(
            newFoodsDistances)
        isFoodNearer = nearestFoodDistance - newNearestFoodDistance

        direction = currentGameState.getPacmanState().getDirection()
        if minGhostDistance <= 1 or action == Directions.STOP:
            return 0
        if scoreDiff > 0:
            return 8
        elif isFoodNearer > 0:
            return 4
        elif action == direction:
            return 2
        else:
            return 1


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (Part 1)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.getNextState(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        # Begin your code (Part 1)

        '''
        First, I initialized and handled the parameter "gameState" that represented
        the first min level list with depth 0 and 1 ghost. Then it started the 
        recursion of swap of max level and min level.

        Second, after judging the current state is win or lose or out of depth range
        every time the max level or min level started, for both of min and max level,
        I always called the next opposite level like min called max. But the difference
        was that for max level the number of ghosts started from 1 with sequent depth, 
        then finding the maximum score. As for min level, min level should handle 
        keep recurring min level until reaching the maximum ghosts, then calling max 
        level next.

        Of course, I handled the exception case that if there was no action the state
        could perform, max level returned infinitely small value (-1e9) and min level 
        returned infinitely big value (1e9).

        Finally, when the recursion finished, then return the maximum value of the first
        min level.
        '''
        pacman = 0
        maxGhost = gameState.getNumAgents()

        def stop(state, curDepth):
            return state.isWin() or state.isLose() or curDepth is self.depth

        def minValue(state, curDepth, numGhost):
            if stop(state, curDepth):
                return self.evaluationFunction(state)

            tmp = []
            for i in state.getLegalActions(numGhost):
                if numGhost is maxGhost - 1:
                    next = state.getNextState(numGhost, i)
                    tmp.append([i, next, maxValue(next, curDepth+1)])
                else:
                    next = state.getNextState(numGhost, i)
                    tmp.append([i, next, minValue(next, curDepth, numGhost+1)])

            if len(tmp) is 0:
                return 1e9

            return min(tmp, key=lambda i: i[2])[2]

        def maxValue(state, curDepth):
            if stop(state, curDepth):
                return self.evaluationFunction(state)

            tmp = []
            for i in state.getLegalActions(pacman):
                next = state.getNextState(pacman, i)
                tmp.append([i, next, minValue(next, curDepth, 1)])

            if len(tmp) is 0:
                return -1e9
            return max(tmp, key=lambda i: i[2])[2]

        action = []
        for i in gameState.getLegalActions(pacman):
            next = gameState.getNextState(pacman, i)
            action.append([i, next, minValue(next, 0, 1)])

        return max(action, key=lambda i: i[2])[0]


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (Part 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        # Begin your code (Part 2)
        '''
        The most things in part 2 was the same as part 1 but some conditional 
        judgement that I found the minimum value of the first min level with 
        alpha maintaining upper bound and beta maintaining lower bound, and 
        in min level, returning the one smaller than the upper bound or considering 
        all the cases, and in max level, returning the one bigger than the 
        lower bound or doing so like min level, and updated upper, lower bound 
        in max, min level respectively.
        '''
        pacman = 0
        maxGhost = gameState.getNumAgents()

        def stop(state, curDepth):
            return state.isWin() or state.isLose() or curDepth is self.depth

        def minValue(state, curDepth, numGhost, a, b):
            if stop(state, curDepth):
                return self.evaluationFunction(state)

            v = 1e9
            for i in state.getLegalActions(numGhost):
                next = state.getNextState(numGhost, i)
                if numGhost is maxGhost-1:
                    v = min(v, maxValue(next, curDepth + 1, a, b))
                else:
                    v = min(v, minValue(next, curDepth, numGhost + 1, a, b))
                if v < a:
                    return v
                b = min(b, v)
            return v

        def maxValue(state, curDepth, a, b):
            if stop(state, curDepth):
                return self.evaluationFunction(state)

            v = -1e9
            for i in state.getLegalActions(pacman):
                next = state.getNextState(pacman, i)
                v = max(v, minValue(next, curDepth, 1, a, b))
                if v > b:
                    return v
                a = max(a, v)
            return v

        action = []
        a = -1e9
        b = 1e9
        v = -1e9
        for i in gameState.getLegalActions(pacman):
            next = gameState.getNextState(pacman, i)
            cal = minValue(next, 0, 1, a, b)
            action.append([i, next, cal])
            if v < cal:
                v = cal
            a = max(a, v)

        return max(action, key=lambda i: i[2])[0]

        # raise NotImplementedError("To be implemented")
        # End your code (Part 2)


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (Part 3)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        # Begin your code (Part 3)
        '''
        This part was almost the same as part 1, too. The difference was that in
        min level, we should return the average instead of the minimum.
        '''

        pacman = 0
        maxGhost = gameState.getNumAgents()

        def stop(state, curDepth):
            return state.isWin() or state.isLose() or curDepth is self.depth

        def minValue(state, curDepth, numGhost):
            if stop(state, curDepth):
                return self.evaluationFunction(state)

            tmp = []
            for i in state.getLegalActions(numGhost):
                if numGhost is maxGhost - 1:
                    next = state.getNextState(numGhost, i)
                    tmp.append(maxValue(next, curDepth+1))
                else:
                    next = state.getNextState(numGhost, i)
                    tmp.append(minValue(next, curDepth, numGhost+1))

            if len(tmp) is 0:
                return 1e9

            return sum(tmp)/len(tmp)

        def maxValue(state, curDepth):
            if stop(state, curDepth):
                return self.evaluationFunction(state)

            tmp = []
            for i in state.getLegalActions(pacman):
                next = state.getNextState(pacman, i)
                tmp.append([i, next, minValue(next, curDepth, 1)])

            if len(tmp) is 0:
                return -1e9
            return max(tmp, key=lambda i: i[2])[2]

        action = []
        for i in gameState.getLegalActions(pacman):
            next = gameState.getNextState(pacman, i)
            action.append([i, next, minValue(next, 0, 1)])

        
        return max(action, key=lambda i: i[2])[0]

        # raise NotImplementedError("To be implemented")
        # End your code (Part 3)

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (Part 4).
    """
    # Begin your code (Part 4)
    '''
    I considered 3 cases such as finding food, fleeing from ghosts, hunting 
    ghosts. Therefore, I set "tmp" as addend and recorded how much it got in
    the 3 cases. 
    
    In food case, "tmp" got 10 time the reciprocal of the minimum distance 
    from all food points. The reason why I chose reciprocal wass I wanted minimum 
    distance to get higher score. 
    
    In fleeing case, "tmp" got -30 time the reciprocal of the minimum distance
    from all the ghosts.

    In hunting case, "tmp" got 100 time the reciprocal of the minimum distance
    from all the ghosts which was reachable in pacman's powerful time after eating
    pellet.

    Using that coefficients, I could get the highest scores after I had tried.
    '''

    newPacPos = currentGameState.getPacmanPosition()
    newPacFood = currentGameState.getFood()

    tmp = 0

    disFood = [1e9]
    for i in newPacFood.asList():
        disFood.append(manhattanDistance(newPacPos, i))

    tmp += 10/min(disFood)

    for i in currentGameState.getGhostStates():
        dis = manhattanDistance(newPacPos, i.getPosition())
        if dis <= 0:
            return -1e9
        
        if i.scaredTimer > 0:
            tmp += 100/dis
            break
        
        tmp += -30 / dis

    return tmp + currentGameState.getScore()
    # raise NotImplementedError("To be implemented")
    # End your code (Part 4)


# Abbreviation
better = betterEvaluationFunction
