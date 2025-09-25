`CMSC 251: Homework 2`

Due date: September 25, 2025 @ 5pm EST.  
Deliverables:  
To be turned in via BrightSpace:

- ‘search.py’: your commented, original code for implementing the search strategies as requested by this assignment, *as well as your implementation of Node*  
  - Be sure to add in header comments the names of any other students you worked with or online resources you accessed (other than checking syntax).  
- ‘Testing.pdf’: a completed PDF copy of [this table](https://docs.google.com/document/d/1HF8ofcqYQgy1aJaJetP3MLMqRcipdXEzsKZfknuJK6o/edit?usp=sharing) that includes your completion of each square in the table  
- ‘Response2.pdf’: your reading response for part 2 of this assignment

	To be turned in via Google Forms:

- [Assignment wrapper](https://docs.google.com/forms/d/e/1FAIpQLSfgwqesk08lFBnooHLtF3sE540hDfUFoct4Z9y0jOK3y4DHpA/viewform?usp=header)

**We are no longer using the Homework Folder (or Git/Github implementation). Email me or drop by office hours (M 1.30pm-2.30pm, Th 11am-12pm) if you have questions.**  
---

**Part 1: Uninformed Search**

*Point values:* 

| DFS basic implementation (def depthFirstSearch) | 3 points |
| :---- | :---- |
| BFS basic implementation (def breadthFirstSearch) | 3 points |
| Uninformed search general method (def uninformedSearch). NOTE: *when you get to this point, comment out your original DFS and BFS implementations so you can use DFS and BFS methods for calls to uninformed search.* (See notes below) | 3 points |
| Submission has appropriate comments, submission is in correct format, assignment wrapper is submissed, etc. | 2 points |

The objectives in this assignment are to become familiar with the two most important search algorithms on graphs: depth-first search (DFS) and bread-first search (BFS).

**Step 1:**

Download search.py and searchAgents.py from BrightSpace and add them to the project directory containing your other pacman code.  You will need to look carefully at three files:

* search.py  —  Your algorithms for this assignment will be located here.  
* searchAgents.py — Your search agents are located here.  
* utils.py — The queue and stack data structures you need are implemented here. If you have not taken data structures, reflect on your lecture notes and feel free to drop by office hours so we can review which of these is appropriate for each search strategy and why.

There is a search agent, SearchAgent, already implemented in searchAgents.py.  This simple agent has a pre-recorded sequence of steps that only works in a very small number of situations.  Note that you may need to run your [search.py](http://search.py) and [searchAgents.py](http://searchAgents.py) before the following commands will work (remember: Python only compiles at runtime, so your tinyMaze is not a “thing” in Python’s eyes until it has been compiled).

You can run it like this from terminal:

| python pacman.py \-l tinyMaze \-p SearchAgent \-a fn=tinyMazeSearch |
| :---- |

Or, you can run it directly from the Spyder IPython Konsole using the format from [the last assignment](https://docs.google.com/document/u/0/d/1Y8sfBcrirSXLtaDe7ekRxKXaMDDrNr6Oxv2D-4qgdg4/edit):

| runfile('pacman.py', args='--layout tinyMaze \--p SearchAgent \-a fn=tinyMazeSearch') |
| :---- |

This specifies a particular agent and a search function to run. Give it a try.

By the way, you can use \--frameTime 0 to run the game most quickly.  This is useful when you are testing and don’t want to wait on the Pac-Man to search a large maze.

**Step 2:**

Your job in this assignment is to implement depth-first search (DFS) and breadth-first search (BFS).  Start with DFS and then generalize and revise your implementation for BFS.

To begin, you will need to write a Node class to support your search strategy.  A Node object contains the state, parent node, action leading to the state, step cost, and path cost.  When writing and testing your DFS function, you must pay attention to the difference between nodes and states.  The state of a searchAgent is its position in the maze, whereas a node (which contains a state) is used to structure the search.  Be sure to comment every class and every method **you** write. Parameters and return types should be clearly explained.  

Once you have DFS working, you can write BFS just by using a different data structure.

You will run the algorithm from terminal like this: python pacman.py \-l tinyMaze \-p SearchAgent \-a fn=dfs  
If you run from the Konsole, you should use runfile('pacman.py', args='--layout tinyMaze \--p SearchAgent \-a fn=dfs')

At the end of this step you should have a working def breadthFirstSearch and def depthFirstSearch.

**Step 3:**

A single algorithm can be used to implement both types of search (DFS and BFS).  We call this UninformedSearch, since it blindly follows a path without using problem information to determine which node to expand next. Here is the pseudocode to guide you.

| function UninformedSearch(problem) returns a list of actions  initialize the frontier using the initial state of the problem  initialize explored to empty \# For explored, use a dictionary                                \# keyed on Pac-Man position, a tuple.  while the frontier is not empty:    choose the next node from the frontier    if the node contains a goal state:      return list of actions from start state to goal state \# solution found    add the state key to the explored dictionary    for each successor of the node state:      if the successor state is not in explored:        add node of the successor onto the frontier  return an empty list \# no solution was found |
| :---- |

In this step you will be writing your own def uninformedSearch. You should comment out (but **keep** your original BFS and DFS implementations) in their respective methods. You will instead be calling uninformedSearch from your depthFirstSearch and breadthFirstSearch methods.

uninformedSearch can implement BSF or DFS, depending on a second parameter, the data structure used to hold the frontier.  Mine looks like this:

| def uninformedSearch(problem,frontierList):   \# Return list of actions that solve the problem using that Stack or Queue as   \# specified by frontierList, which is a util.Stack or util.Queue.  ... |
| :---- |

The calls to depthFirstSearch(problem) and  breadthFirstSearch(**problem)** will then simply call uninformedSearch with frontierList set appropriately. Again,  at this point you should comment out (but leave in your search.py file) your original DFS and BFS implementations.

If you are not successful with step 3, you should write (in comments) in the body of def uninformedSearch how you tried to approach the problem, or what you tried, and why you think it didn’t work. If you run out of time (start assignments early\!) you can explain how you would attempt to implement uninformedSearch.

**Step 4:**

You should then complete the table linked in the assignment header that compares the MazeType with the various searching algorithms. If you do not get step 3 working, you should run this step with your original, working DFS and BFS methods (i.e., do not call uninformedSearch from your DFS and BFS methods).

---

**Part 2: Reading Reflection**

*Point value: 3 points.*

It seems like everyone is talking about “vibe coding”. Some people are thrilled, others are skeptical. 

*Read the following articles and 1\) briefly explain, in your own words, what vibe coding is, then, 2\) take a position in favor of vibe coding – why is it good?, and finally, 3\) take the opposite position – why is vibe coding bad?* 

Your answer should be no more than 300 words. You should refer to the provided texts as well as add your own original insight. Off-topic responses or responses that do not follow the provided structure (brief explanation, positive position, negative position) will not receive credit.

You may find it helpful to consider the priorities of different groups in formulating your argument. For example, you could consider an artist who wants to write programs to support a larger project, but does not want to learn a new programming language (or who may not know how to code at all). You could consider Big Tech CEOs: what are their incentives? Think about a junior programmer, who is just learning how to do things, and a senior programmer, who is in charge of reviewing a junior programmer’s code. 

Suggested articles – you can use other sources to support your argument, please include the link to them in your writeup:

1. [What is Vibe Coding (IBM)](https://www.ibm.com/think/topics/vibe-coding)  
2. [Vaugh-Nichols, Against Vibe Coding](https://drive.google.com/file/d/1KCgGDwJJ_1JKaMgvh8pbMt9UshNiQgZB/view?usp=drive_link)  
3. [Tan, OpenAI Research Head on Vibe Coding](https://drive.google.com/file/d/1jNMRcmcpdJZBRzbEgOXf_qgKlsE_q3cJ/view?usp=drive_link)

