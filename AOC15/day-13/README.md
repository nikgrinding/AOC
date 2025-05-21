## Part 1

We are given happiness scores between pairs of people depending on whether they sit next to each other at a circular dinner table. Our goal is to find the optimal seating arrangement that maximizes the total happiness.

Each line describes how a person's happiness would increase or decrease if they were to sit next to another specific person.

**Example:**
Alice would gain 54 happiness units by sitting next to Bob  
Bob would lose 7 happiness units by sitting next to Carol  

Optimal arrangement: Alice → Bob → Carol → David → Alice  

In this setup, we calculate happiness in both directions for each adjacent pair. For example, if Alice sits next to Bob, the total impact is Alice→Bob + Bob→Alice.

### Idea
Parse the happiness changes into a matrix and try every permutation of seatings (circular, so fix one person to reduce duplicates). For each permutation, compute the total happiness by adding the pairwise values in both directions and keep track of the maximum.

## Part 2

We now include ourselves at the table. Since we are neutral, every pair involving us contributes 0 happiness change. We need to recalculate the best seating including this new person.

### Idea
Add a new person ("You") to the happiness matrix with 0 values for all interactions. Then rerun the same permutation logic to find the new optimal arrangement.