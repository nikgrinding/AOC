## Part 1

We are given a list of container sizes and a total volume of eggnog to store. Each container must be used entirely or not at all. We want to determine how many different combinations of containers sum up exactly to the target volume (e.g., 150 liters).

**Example:**
Input:
```
Containers: [20, 15, 10, 5, 5]
Target: 25
```
Output:
```
4
```
(The combinations are: 15+10, 20+5 (first 5), 20+5 (second 5), and 15+5+5)

### Idea
Use dynamic programming to track how many ways we can reach every possible volume up to the target. For each container, update the number of ways we can form each volume using it. At the end, return the number of ways to form exactly the target volume.


## Part 2

We now want to find how many of those valid combinations use the **minimum number of containers** possible.

**Example:**
Input:
```
Containers: [20, 15, 10, 5, 5]
Target: 25
```
Output:
```
3
```
(Minimum number of containers is 2, and there are three such combinations: 15+10, 20+5 (twice))

### Idea
Try all possible combinations of containers (from size 1 to N). For each combination, check if the total volume equals the target. Keep track of how many combinations use each possible number of containers. Return the count corresponding to the **minimum** number of containers that yields the target volume.