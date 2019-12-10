# alg-midtern review

**record outline**

- lecture01_Introduction.pptx
    + mainly reference : introduction to algorithm
    + promise: at least one question is similar to the hw
    + source: cs161.standford.edu
    + Integer Multiplication
    + Asymptotic Analysis and big-O notation
- lecture01_karatsuba.ipynb
    + multiplication test
- lecture02_insertion_merge_sort.pptx
    + Sort
        - merge
        - insertion
        - proof of induction
        - ex of polynomial
- lecture02_sorting.ipynb
    + comparation of merge-sort and insertion-sort
- lecture03_master theorem_substitution method.pptx
    + recurrence relations
    + the master method
    + substitution method(more general)
- lecture04.ipynb
    + substitution theory
- lecture04auxFile.py
    + merge-sort time record
- lecture04_selection problem.pptx
    + more practise with the substitution method
        - guess what the answer is
        - prove by induction that your guess is correct
        - profit
    + k-select problem
        - that is the benchmark of the MergeSort
        - idea: divide and conquer
        - pick up the median pivot, it seems that it will work with las vegas wrapper
    + k-select solution
        - ```py
          if len(A) <= 50:
              A = MergeSort(A)
              return A[k-1]
          p = getPivot(A)
          L, pivotVal, R = Partition(A,p)
          if len(L) == k-1:
              return pivotVal
          elif len(L) == k - 1:
              return Select(L,K)
          elif len(L) < k - 1:
              return Select(R,k - len(L) - 1)
          ```
    + return of the substitution method
- lecture05auxFile.py
    + something related with sorting a bunch
- lecture05DivideAndConquerI.pdf
    + divide and conquer
    + application repeat and some quiz about detail of some algorithm like quicksort
    + consider BST
    + more problem: closest pair, farthest pair, convex hull, Delaunay/Voronoi, Euclidean MST
- lecture05DivideAndConquerII.pdf
    + master theorem
    + integer multiplication
    + matrix multiplication
    + convolution and FFT
- lecture05_quicksort.ipynb
    + some code and plot by quicksort
- lecture05_Randomized Algorithms and QuickSort.pptx
    + comparation between QuickSort vs MergeSort
- lecture06DynamicProgrammingI.pdf
    + weighted interval scheduling
    + segmented least squares
    + knapsack problem
    + RNA secondary structure
- lecture06DynamicProgrammingII.pdf
    + sequence alignment
    + Hirschberg's algorithm
    + Bellman-Ford-Moore algorithm
    + distance-vector protocols
    + negative cycles
- lecture06_Graphs, BFS and DFS.pdf
    + graphs and terminology
    + Depth-first search
        - App: topological sorting
        - App: in-order traversal of BSTs
    + Breadth-first search
        - App: shortest paths
        - App(if time): is a graph bipartite
- lecture07_Finding Strongly Connected Components.pdf
    + breadth-first and depth-first search
    + property
- lecture07_scc.ipynb
    + strongly connected components
- lecture08_Dijkstra's Algorithm and Bellman-Ford.pdf
    + Dijkstra
    + Bellman-Ford
- lecture09_Dynamic Programming.pdf
    + warm-up: Fibonacci numbers
- lecture09_Graphs, BFS and DFS.pdf
    + Floyd-Warshall Algorithm
- lecture09_graphs.ipynb
    + graph and some other thing
- lecture10_More dynamic programming.pdf
    + Longest common subsequence
    + knapsack
    + independent sets in trees
- lecture11_Greedy Algorithms.pdf
    + Make choices one-at-a-time
    + Never look back
    + Hope for the best
- lecture11_greedy.ipynb
    + greedy app
- lecture12_Minimum Spanning Trees.pdf
    + definition of minimum spanning tree
    + short break to introduce some graph theory tools
    + Prim's algorithm
    + Kruskal's algorithm
- lecture12_mst.ipynb

**guess test point**

- Multiplication
    + divide and conquer
    + how to use big-O notation
    + naive: m n m*n+m*n
    + karatsuba: divide (a* 10^(m/2) + b)(c*10^(n/2) + d) = ac 10 (bc+ad) bd
- Insert-Sort
    + idea: sub_problem sort had small sorted list we have one to insert so that it could be sorted.
    + time complexity: n^2
- Merge-Sort
    + idea: divide equally two part and make a double check
    + log(n) * n
- Proof of induction about O
    + How to calculate polynomial
    + find c
    + use contrast proof
- master theorem
    + https://blog.csdn.net/lanchunhui/article/details/52451362
- substitution method
    + guess
    + proof mathematical iteration inductive
    + profit
- k-select solution
    + ignore half and focus another part
- quick-sort
    + just like k-select
- Divide and conquel multiple choice question
    + 
- More problem: closest pair, farthest pair, convex hull, Delaunay/Voronoi, Euclidean MST
- Matrix multiplication
    + https://www.jianshu.com/p/dc67e4a3c841
    + divide and make 8 sub-multiplication into 7
- convolution and FFT
    + https://www.cnblogs.com/rvalue/p/7351400.html
- weighted interval scheduling
    + https://www.jianshu.com/p/3e230492b9c7
- knapsack problem
    + idea: small bag
- sequence alignment
    + brute force
    + matrix saving sub-problem
- LCS
    + https://blog.csdn.net/qq_34153219/article/details/71698475
- SHORTEST PATH
    + https://www.cnblogs.com/gaochundong/p/bellman_ford_algorithm.html
    + Dijkstra https://blog.csdn.net/kprogram/article/details/81225176
    + Bellman-Ford
    + FW-Algorithm https://blog.csdn.net/ideaqjx/article/details/78881044
- GRAPH
    + BFS
    + DFS
    + SCC https://www.cnblogs.com/soTired/p/5116815.html
- Independent sets in trees
