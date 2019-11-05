# algorithm lecture note for week 8
## warmup
- emphsize the doing thing skill
- proof with induction

## homework
- hint: polynomial and convolution related lighly with Fast Fourier transformation.
- construct a polynomial product and make a total force at the same coefficient.

## Graph search
- to do list
    + find PPT and write down the key point -done
    + have a fast review on today lecture and get key concpet and get known to what's the problem and mindgraph.
    + find similiar concept in the reference book
- outline
    + Graphs and terminology
    + Depth-first search
        * App, topological sorting
        ```
        L <- Empty list that will contain the sorted elements
        S <- Set of all nodes with no incoming edge
        while S is non-empty do
            remove a node n from S
            add n to tail of L
            for each node m with an edge e from n to m do
                remove edge e from graph
                if m has no other incoming edges then 
                    insert m into m
        if graph has edges then
            return error (graph has at least one cycle)
        else
            return L (a topologically sorted order)
        ```
        * App, in order traversal of BSTs
    + Breadth-first search
        * App, shortest paths
        * App, bipartite

### Graphs and terminology
- class: undirected or directed
- representation
    + adjacency matrix
    + adjacency lists
    + trade offs

### Depth First Search
- another application: finding strongly connected components

    a directed graph G = (V,E) is strongly connected if

    for all v,w in V there is path from v to w and thee is a path from w to v
- why do we care about SSCs

    Strongly connected components tell you about communities

    Lots of graph algorithms only make sense on SCCs
- One straightforward solution with $\Theta(n^{2})$ running time.

```
SCCs = []
For each u:
    Run DFS from u
    For each vertex v that u can reach:
        if v is in an SCC we've already found:
            Run DPF from v to see if you can reach u
            if so, add u to v's SCC
            Break
    If we didn't break, create a new SCC which just contains u.
```

- a method with $\Theta(n+m)$ running time.

```
Do DFS to create a DFS forest.
    choose starting vertices in any order
    keep track of finishing times
Reverse all the edges in the graph
Do DFS again to create another DFS forest.
    This time, order the nodes in the reverse order of the finishing times that they had from the first DFS run.
The SCCs are the different trees in the second DFS forest.
```

- a new question: pretend that each SCC is a vertex in a new graph
    + Lemma 1: The SCC graph is a directed acyclic graph
    + Starting and finishing times in a SCC
    + more property of SCC DAG

### Weighted Graphs: Dijkstra and Bellman-Ford
**outline**

