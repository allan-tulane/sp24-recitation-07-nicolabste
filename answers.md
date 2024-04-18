# CMPS 2200 Recitation 10## Answers

**Name:** Nicolas Labarca
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**

The work function W(n,m) = W(2m) + W(n)+1 is bounded by O(n+m).

- **4)**

The reachable function is designed to be invoked just once per graph, determining if the graph is connected (returning true) or disconnected (returning false). Consequently, it is called only once under any scenario.

- **5)**

The function W(n,m) defined as W(2m) + W(n) + O(1) +1 falls within the complexity class O(n+m).

- **7)**

Switching the graph representation to an adjacency matrix alters the complexity of operations. Specifically, identifying all adjacent nodes of a given node becomes an O(n) operation by simply scanning that node's row in the matrix. Therefore, checking adjacency for all nodes requires examining every matrix element, leading to a total computational cost of O(n^2)
