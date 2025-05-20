## Part 1

Santa needs to visit a number of cities exactly once, choosing any starting and ending point.
The elves have provided the pairwise distances between all cities.

The task is to determine the **shortest possible route** that visits each city exactly once.

**Example**

Input:
```
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
```

Output:
```
605
```

### Idea

We treat this as a variation of the Traveling Salesman Problem (TSP). We generate all permutations of the cities
and compute the total distance of each route. The answer is the minimum of all these route costs.

## Part 2

Santa now wants to find the **longest possible route** that visits each city exactly once instead of the shortest.

**Example**

Input:
```
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
```

Output:
```
982
```

### Idea

This part is similar to Part 1, but instead of minimizing the total cost, we maximize it.
We compute the cost for every possible permutation and return the maximum route length.