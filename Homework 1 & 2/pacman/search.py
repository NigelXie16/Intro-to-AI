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

class Node:
    def __init__(self, state, parent=None, action=None, stepCost=0, pathCost=0):
        self.state = state # the state of the node
        self.parent = parent # the parent node
        self.action = action # the action to reach the state
        self.stepCost = stepCost # the cost to the next state
        self.pathCost = pathCost # total cost of the path so far ?

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

def uninformedSearch(problem, frontier):
    start = problem.getStartState() # get the start state

    frontier = frontier # util.Stack() or util.Queue() storing the nodes to be expanded
    explored = set() # set of states that have been explored

    frontier.push(Node(start)) # add the start state to the frontier

    while not frontier.isEmpty():
        
        # pop the next node from the frontier
        node = frontier.pop()         

        # check if the node is a goal state
        if problem.isGoalState(node.state): 
            # Reconstruct the path by backtracking
            path = []
            while node.parent is not None: # traces up to the start state
                path.append(node.action)
                node = node.parent
            path.reverse() # reverse the path to get the correct order
            return path

        # Add the node to the explored set
        explored.add(node.state)

        # Add successors of the node to the frontier
        for successor, action, stepCost in problem.getSuccessors(node.state):
            if successor not in explored:
                frontier.push(Node(successor, node, action, stepCost, node.pathCost + stepCost))
    return [] 

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    return uninformedSearch(problem, util.Stack())

    start = problem.getStartState() # get the start state

    frontier = util.Stack() # LIFO stack storing the nodes to be expanded
    explored = set() # set of states that have been explored

    frontier.push(Node(start)) # add the start state to the frontier

    while not frontier.isEmpty():
        node = frontier.pop() # pop the next node from the frontier
        if problem.isGoalState(node.state): # check if the node is a goal state
            # Reconstruct the path by backtracking
            path = []
            while node.parent is not None: # traces up to the start state
                path.append(node.action)
                node = node.parent
            path.reverse() # reverse the path to get the correct order
            return path

        # Add the node to the explored set
        explored.add(node.state)

        # Add successors of the node to the frontier
        for successor, action, stepCost in problem.getSuccessors(node.state):
            if successor not in explored:
                frontier.push(Node(successor, node, action, stepCost, node.pathCost + stepCost))
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    return uninformedSearch(problem, util.Queue())

    start = problem.getStartState() # get the start state

    frontier = util.Queue() # FIFO queue storing the nodes to be expanded
    explored = set() # set of states that have been explored

    frontier.push(Node(start)) # add the start state to the frontier

    while not frontier.isEmpty():
        node = frontier.pop() # pop the next node from the frontier
        if problem.isGoalState(node.state): # check if the node is a goal state
            # Reconstruct the path by backtracking
            path = []
            while node.parent is not None: # traces up to the start state
                path.append(node.action)
                node = node.parent
            path.reverse() # reverse the path to get the correct order
            return path

        # Add the node to the explored set
        explored.add(node.state)

        # Add successors of the node to the frontier
        for successor, action, stepCost in problem.getSuccessors(node.state):
            if successor not in explored:
                frontier.push(Node(successor, node, action, stepCost, node.pathCost + stepCost))
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

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
