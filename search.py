# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #starting point of pac-man
    (x,y) = problem.getStartState()

    #to check whether a point is visited or not
    visited = {}
    visited[(x,y)]= True

    #path map.
    map={}
    stack = util.Stack()
    for successor in problem.getSuccessors(problem.getStartState()):
        stack.push(successor)
        map[successor[0]]=((x,y),successor[1])

    #result list consists the directions.
    res_list=[]

    #while stack is not empty, loop over it.
    while not stack.isEmpty():
        cur_state = stack.pop()
        cur_x,cur_y = cur_state[0][0],cur_state[0][1]

        #check whether current point is not visited and make it as true.
        if (cur_x, cur_y) not in visited:
            visited[(cur_x, cur_y)] = True

            #if current point is goal state , loop over map and return the path.
            if problem.isGoalState((cur_x,cur_y)):
                while cur_x!=x or cur_y!=y:
                    ele = map[(cur_x,cur_y)]
                    res_list.append(ele[1])
                    (cur_x,cur_y) = ele[0]
                res_list.reverse()
                print "length of list :", len(res_list)
                return res_list

            #if neighbours are not visited , push them to stack.
            for neighbour in problem.getSuccessors((cur_x,cur_y)):
                if (neighbour[0][0], neighbour[0][1]) not in visited:
                    stack.push(neighbour)
                    map[neighbour[0]] = ((cur_x,cur_y),neighbour[1])
    return res_list

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # starting point of pac-man
    (x, y) = problem.getStartState()

    # to check whether a point is visited or not
    visited = {}
    visited[(x, y)] = True

    # path map.
    map = {}
    queue = util.Queue()
    for successor in problem.getSuccessors(problem.getStartState()):
        queue.push(successor)
        map[successor[0]] = ((x, y), successor[1])

    # result list consists the directions.
    res_list = []

    # while queue is not empty, loop over it.
    while not queue.isEmpty():
        cur_state = queue.pop()
        cur_x, cur_y = cur_state[0][0], cur_state[0][1]

        # check whether current point is not visited and make it as true.
        if (cur_x, cur_y) not in visited:
            visited[(cur_x, cur_y)] = True

            # if current point is goal state , loop over map and return the path.
            if problem.isGoalState((cur_x, cur_y)):
                while cur_x != x or cur_y != y:
                    ele = map[(cur_x, cur_y)]
                    res_list.append(ele[1])
                    (cur_x, cur_y) = ele[0]
                res_list.reverse()
                print "length of list :", len(res_list)
                return res_list

            # if neighbours are not visited , push them to queue.
            for neighbour in problem.getSuccessors((cur_x, cur_y)):
                if (neighbour[0][0], neighbour[0][1]) not in visited:
                    queue.push(neighbour)
                    map[neighbour[0]] = ((cur_x, cur_y), neighbour[1])
    return res_list

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
