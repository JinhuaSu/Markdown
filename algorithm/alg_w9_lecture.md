# lecture of algorithm in week 9

**target**

- prepare for the midterm exam
- indeed i should keep my path or listen to the teacher
- however, now to listen to teacher may not be good for I have been lagged off.

**to_do_list**

- check teacher lecture title and download some new slides from the 163-mailbox -done
- write down all the key word and concept -done
    + order: graph to the latest then return
- ask myself a question whether i need to get chinese interpretation
    + Bellman-Ford alg
    + DFS
- each by each learn chinese tutorial
- then have a soon glimpse

## learning roadmap

**programming skill**

- learn something in the ipython
- convert the pseudo code into python code

**mindgraph for solving alg-problem**
- work or not
- is it fast enough
- how to improve it

**keyword**

1. intro
2. sort
    - insertion
    - merge
3. theorem about time complexity
    - master theorem
    - substitution method
4. selection problem
5. quicksort & randomized algorithm & divide and conquer
    - randomize proof
    - k-select
6. Graphs, BFS and DFS & DynamicProgramming
    - BFS: shortest way for equaling weights graph
    - DFS
        + start time
        + finish time
    - app: topological
    - ?DP：scracrify space for time efficiency improving
        + several quiz for review
        + top down
        + bottom up
7. finding strongly connected components
    - the application of DFS 
    - DFS tree
8. Dijkstra's Algorithm and Bellman-Ford
    - positive weight
    - Bellman-Ford is an algorithm: no matter whether there is circle & negative weight or not, so it is a more general algorithm. However it is a bit slower than Dijkstra's Algorithm.
9. Dynamic Programming & graph
    - search with weight
10. More dynamic programming

**learning note**

- Bellman-Ford alg
    + problem: how to find shortest rounte for a graph with negative weight, where dijkstra may give a discorrect result.
    + concept：negative weight means passing it will decrease the total cost. If negative weight appear in the undirected graph, there will be no shortest route while it still has a solution when negative weight doesn't make up of a circle in the directed graph.
    + naive solution: monte-calo way for trying and give a biased estimated or inspired by the dijkstra alg(BFS and relax using edge but small order how to decrease unnecessary time cost).
    + pseudo code
    ```
    def BF(node_num,D_M)
    D = [0 if i  for]
    for e
    ```
    