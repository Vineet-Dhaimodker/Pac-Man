Artificial Intelligence, Pacman Game (Fall 2016)
======================================

## Intro
[The Pacman Projects](http://ai.berkeley.edu/project_overview.html) by the [University of California, Berkeley](http://berkeley.edu/).

![Animated gif pacman game](http://ai.berkeley.edu/images/pacman_game.gif)

> In this project, Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently. Try to build general search algorithms and apply them to Pacman scenarios.

Start a game by the command:
```
$ python pacman.py
```
You can see the list of all options and their default values via:
```
$ python pacman.py -h
```

## Search Problems
- DFS, BFS, UCS, ASTAR, ASTAR heuristic 
```
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfs
$ python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
$ python pacman.py -l bigMaze -p SearchAgent -a fn=ucs
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
- Corner problem, Corner heuristic
```
$ python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
$ python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
- Eating all the dots
```
$ python pacman.py -l trickySearch -p AStarFoodSearchAgent
```

<!-- > for more information, check [here](https://github.com/jasonwu0731/NTU-AI-Fall2016/blob/master/Pacman/hw1-search/Project1.html) for details -->

