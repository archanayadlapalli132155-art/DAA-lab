practical:2 
Linear Search Summary:
Linear Search is a simple searching algorithm that checks each element of an array one by one from the beginning until the required element is found or the end of the array is reached. 
It can be used on both sorted and unsorted data.
The number of comparisons depends on the position of the searched element.
Best Case: O(1)
Average Case: O(n)
Worst Case: O(n)
Space Complexity: O(1)

Linear Search Conclusion :
Linear Search is easy to implement and suitable for small or unsorted datasets.
However, its performance decreases as the size of the dataset increases because it may need to check every element.
Therefore, it is less efficient for searching large datasets.

binary search summary :
Binary Search is an efficient searching algorithm that works by repeatedly dividing a sorted array into two halves.
It compares the search element with the middle element and eliminates the half that cannot contain the required element. 
This process continues until the element is found or the search range becomes empty.
Best Case: O(1)
Average Case: O(log n)
Worst Case: O(log n)
Space Complexity: O(1) for the iterative implementation

binary search conclusion :
Binary Search is significantly more efficient than Linear Search for large sorted datasets because it reduces the search space by half at every step. 
Its main limitation is that the data must be sorted before searching. 
Therefore, Binary Search is particularly useful when searching repeatedly in a large sorted dataset.

practical 3:
Summary :
Max Heap Sort is a sorting algorithm based on the Max Heap data structure.
First, the given array is converted into a max heap, where the largest element is present at the root.
The root is then exchanged with the last element, and the remaining heap is adjusted using the heapify operation.
This process is repeated until the entire array is sorted in ascending order.

Conclusion :
Max Heap Sort provides a reliable sorting technique with a time complexity of O(n log n) in the best, average, and worst cases. 
It is also an in-place sorting algorithm, requiring only O(1) auxiliary space apart from the recursion used in this implementation.
Therefore, Heap Sort is useful when predictable performance and low additional memory usage are important.

practical 4:
Summary :
The factorial of a number was implemented using both iterative and recursive methods in Python.
The iterative approach uses a for loop to multiply numbers from 1 to n, while the recursive approach repeatedly calls the same function until it reaches the base case.
Both methods have a time complexity of O(n), but the iterative method requires only O(1) extra space, whereas the recursive method requires O(n) stack space.

Conclusion :
Both iterative and recursive methods correctly calculate the factorial of a non-negative integer. 
The iterative method is more memory-efficient because it does not create recursive function calls. 
The recursive method provides a direct representation of the mathematical definition of factorial and is useful for understanding recursion.
For practical computation, the iterative method is generally preferable when avoiding additional call-stack usage is important.


practical 6:
Summary :
Chain Matrix Multiplication is an optimization problem in which the objective is to determine the most efficient order for multiplying a sequence of matrices.
Since matrix multiplication is associative, different parenthesizations produce the same result but may require different numbers of scalar multiplications.
The Dynamic Programming approach divides the problem into smaller subproblems, stores their results, and uses them to calculate the optimal solution. 
The program maintains a cost table m[i][j] to store the minimum multiplication cost for each matrix chain.

Conclusion :
The Chain Matrix Multiplication problem was successfully implemented using Dynamic Programming.
The algorithm determines the optimal order of matrix multiplication while minimizing the number of scalar multiplications.
For n matrices, the algorithm has:
Time Complexity: O(n³)
Space Complexity: O(n²)


practical 7:
Summary :
The Making Change Problem is a classic optimization problem that can be efficiently solved using Dynamic Programming.
A DP array is created where each position stores the minimum number of coins required to form that particular amount.
The solution for larger amounts is obtained from previously calculated smaller amounts.
In the given example, the denominations are [1, 2, 5, 10] and the target amount is 27.
The algorithm determines that only 4 coins are required: 10 + 10 + 5 + 2.

Conclusion :
Dynamic Programming provides an efficient solution to the Making Change Problem by storing previously calculated results and avoiding repeated calculations.
The algorithm is simple to implement and works well for different coin denominations and target amounts. 
It demonstrates the important DP concepts of optimal substructure and overlapping subproblems.


practical 8:
BFS — Breadth-First Search
Summary :
Breadth-First Search (BFS) is a graph traversal algorithm that visits nodes level by level.
It starts from a selected node and first visits all its neighboring nodes before moving to the next level. 
BFS uses a queue (FIFO) data structure to keep track of the nodes that need to be visited.
It is commonly used for finding the shortest path in an unweighted graph, network traversal, and finding nodes at a particular distance.

Conclusion :
BFS provides a systematic way to traverse a graph by exploring nodes level by level. 
It is simple to implement using a queue and is particularly useful when the shortest path in terms of the number of edges needs to be found. 
In our implementation, BFS successfully traversed the graph starting from node A and produced the traversal order:
A → B → C → D → E → F

DFS — Depth-First Search
Summary :
Depth-First Search (DFS) is a graph traversal algorithm that explores a graph by going as deep as possible along one path before backtracking.
DFS can be implemented using a stack or recursion. 
It is useful for exploring connected components, solving mazes, detecting cycles, and other graph-related problems.

Conclusion :
DFS provides an effective method for exploring a graph by following one branch deeply before moving to another branch.
It uses recursion or a stack to keep track of the traversal.
In our implementation, DFS successfully traversed the graph starting from node A and produced the traversal order:
A → B → D → E → F → C


practical 9:
Summary :
Prim's Algorithm is a greedy approach for finding the Minimum Spanning Tree of a connected, weighted, undirected graph.
It starts with any vertex and repeatedly selects the minimum-weight edge that connects a visited vertex to an unvisited vertex. 
This process continues until all vertices are included in the spanning tree.

Conclusion :
Prim's Algorithm successfully constructs a Minimum Spanning Tree while ensuring that all vertices are connected with the minimum possible total edge weight and without forming cycles.
It is useful in applications such as network design, cable connections, road networks, and communication systems, where the goal is to connect all locations with minimum cost.
