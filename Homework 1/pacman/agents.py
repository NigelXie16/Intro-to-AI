#**************************************************************************
# Results:
# RandomAgent: 1993, 621, 1578, 1777, 2646, 592, 1107, 1120, 902, 761
# 	Mean: 
# 	STDDev: 
# ReflexAgent: 333, 203, 363, 733, 356, 418, 279, 588, 206, 298
# 	Mean: 
# 	STDDev: 
#
# Try to explain the differences in agent performance that you observe.  
# You should document your statistical results and provide a one paragraph comparison in a comment section at the top of agents.py
# 
# The ReflexAgent eats all the food with significantly less steps, aka performs better, because fundamentally 
# ReflexAgent Perform the next action that aligned with our goal state of complete food consumption. That is, 
# the RandomAgent moves acts randomly no matter how the food spread or whether food can be reached via the next action, 
# while RandomAgent prioritizes those actions that lead to food. While steps spent in empty spaces without food in the next action, 
# are redundant steps in both agents. ReflexAgent forms a consecutive path eating food consecutively. 
# Which is also reflected in the score that Pono's time spent wandering around.
# 
#**************************************************************************

from enum import nonmember
import random
from game import Agent
from game import Directions
from game import Actions

class BasicAgent(Agent):
  """This agent just heads North until it cannot move"""
  def getAction(self, state):
    legal = state.getLegalPacmanActions() # get the legal actions
    if Directions.NORTH in legal: # if North is in the legal actions
      return Directions.NORTH # return North
    else: # if North is not in the legal actions
      return Directions.STOP # return Stop

class RandomAgent(Agent):
  """This agent chooses a random action to perform out of all the legal actions"""
  def __init__(self):
    self.steps = 0 # int to count the number of steps
  
  def getAction(self, state):
    legal = state.getLegalPacmanActions()
    if legal:
      # remove STOP from legal
      non_stop_actions = [action for action in legal if action != Directions.STOP] # remove Stop from the legal actions
      if non_stop_actions: # if Pacman can take non-stop actions
        self.steps += 1 # increment the number of steps
        print(self.steps) # print the number of steps
        return random.choice(non_stop_actions)
    else: # if Pacman cannot take non-stop actions, print steps and Stop
      print("it took ", self.steps, " steps to finish using RandomAgent")
      return Directions.STOP

class ReflexAgent(Agent):
  """A Reflex Agent [5 pts]
Now lets make the Pac-Man a bit smarter.  We can do this by allowing it to observe percepts within its environment.  

Using the state variable, the following percepts are possible:

pac-man position
position of ghosts
wall locations
capsule locations
food location
number of food pellets remaining
current score
whether it has won or lost

Create a new ReflexAgent with agents.py.   This agent should examine possible legal one-step moves, except Stop, and select a random one of those that has a food pellet.  If none has a food pellet, a random action (but not Stop) should be returned.
"""
  def __init__(self):
    self.steps = 0 # int to count the number of steps

  def getAction(self, state):
    legal = state.getLegalPacmanActions() # get the legal actions
    # exclude Stop from the legal actions
    non_stop_actions = [action for action in legal if action != Directions.STOP]
    if not non_stop_actions: # if there is no more action than stop to take
      print("it took ", self.steps, "steps to finish using ReflexAgent")
      return Directions.STOP

    # map all directions to vectors, adding with the Pacman's coordinates to locations of next actions, 
    # compare the next actions / evaluate whether they have food, put it into a new list, and proceed to make action
    food = state.getFood() # food[x][y] is true if there is food there
    px, py = state.getPacmanPosition() # get the x, y position of Pacman

    food_actions = [] # list to store actions that leds to food
    for a in non_stop_actions:
      dx, dy = Actions.directionToVector(a) # convert each of the non_stop_actions to vecter representation
      x, y = int(px+dx), int(py+dy) # derive the next state locations of Pacman for each of the possible actions
      if food[x][y]: # if the location have food / maps to true in food[][] Grid map
        food_actions.append(a)

    if food_actions: # if any moves lands on food
      self.steps += 1
      print(self.steps)
      return random.choice(food_actions) # Choose randomly to perform

    self.steps += 1
    print(self.steps)
    return random.choice(non_stop_actions) # Otherwise no food surrunds Pacman, Choose among all the non_stop_actions

# for a more goal focused agent, that is to eat all food, a index for each of the direction can be calculated, 
# using all the foods' coordinates, to derive a direction that will lead to more food in general. 