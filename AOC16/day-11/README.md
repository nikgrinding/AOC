## Part 1

You need to move several pairs of microchips and their corresponding generators to the fourth floor of a building using an elevator. The elevator can carry one or two items and moves one floor at a time. Microchips get fried if they are with another generator and their own generator isn’t present. You're asked to find the minimum number of moves to bring all items to the fourth floor without violating any constraints.

**Example:**
```
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
```

In this example, the minimum number of moves is 11.

### Idea

We treat this as a shortest path search using BFS where each state consists of the current elevator floor and the floors of all item pairs. We normalize states to avoid revisiting equivalent configurations. At each step, we generate all valid combinations of one or two items to move, try moving them up or down, and only continue if the resulting state is valid. We return the number of steps when all items are on the fourth floor.

## Part 2

The problem is extended with two extra components: an elerium generator and microchip, and a dilithium generator and microchip, both starting on the first floor. The goal is still to bring all items to the fourth floor safely.

### Idea

We extend the same BFS approach from Part 1 with the initial state now including the four new items. The search space becomes larger, but the state representation and validation remain the same. The algorithm efficiently finds the shortest sequence of valid moves to bring all items to the top.