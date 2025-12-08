# Day 8: Playground

## Part 1

The problem involves connecting junction boxes in 3D space to form electrical circuits. You have a list of junction box positions and need to connect them by always choosing the two **closest unconnected junction boxes** (based on straight-line distance). The goal is to make a specific number of connections and then calculate a value based on the resulting circuit sizes.

**Input format:** Each line contains three comma-separated integers representing the X, Y, Z coordinates of a junction box.

**Rules and constraints:**

-   Connect junction boxes pairwise, always selecting the two closest boxes that aren't already directly connected
-   When two boxes are connected, electricity can flow between them (they become part of the same circuit)
-   If both boxes are already in the same circuit, connecting them does nothing
-   Make exactly 1000 connections for the actual input (10 for the example)

**Example:**

```
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
```

**Explanation:**

1. Connect `162,817,812` and `425,690,689` (closest pair) -> 1 circuit with 2 boxes, 18 individual circuits
2. Connect `162,817,812` and `431,825,988` (next closest) -> 1 circuit with 3 boxes, 17 individual circuits
3. Connect `906,360,560` and `805,96,715` -> 1 circuit with 3 boxes, 1 circuit with 2 boxes, 15 individual circuits
4. Try to connect `431,825,988` and `425,690,689` -> No change (already in same circuit)
5. Continue this process...

After 10 connections, there are 11 circuits:

-   1 circuit with 5 boxes
-   1 circuit with 4 boxes
-   2 circuits with 2 boxes each
-   7 circuits with 1 box each

**Expected output:** `5 * 4 * 2 = 40`

### Idea

1. Parse and **calculate all distances** by converting the input to 3D coordinates and create all possible pairs of junction boxes, sorting them by Euclidean distance
2. Track circuits with **a version of DSU**, here a dictionary mapping each junction box to its circuit ID, merging circuits when connecting boxes from different circuits
3. Make the N connections by iterating through the sorted pairs, connecting the closest unconnected pairs and updating circuit memberships
4. Count the size of each circuit, find the three largest, and multiply them together

## Part 2

Instead of making exactly 1000 connections, Part 2 requires you to **keep connecting junction boxes until they all form a single circuit**. The output changes from multiplying circuit sizes to multiplying the X coordinates of the final two boxes that complete the circuit.

**Modified constraint:**

-   Continue connecting pairs until all junction boxes belong to one unified circuit
-   Return the product of the X coordinates of the last two boxes connected

**Example:**

Using the same input as Part 1, continue making connections beyond the first 10. The connection that finally unifies all boxes into a single circuit is between `216,146,977` and `117,168,530`.

**Expected output:** `216 * 117 = 25272`

### Idea

1. Parse coordinates and sort all pairs by distance
2. Connect until unified by iterating through the pairs, updating circuit memberships until all boxes share the same circuit ID
3. **Track the final connection** by checking after each connection if there's only one unique circuit ID remaining
4. When unified, multiply the X coordinates of the last two connected boxes
