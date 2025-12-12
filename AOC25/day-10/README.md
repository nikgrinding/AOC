# Day 10: Factory

## Part 1

Factory machines need to be initialized by configuring their indicator lights to match specific patterns. Each machine has indicator lights (initially all off) and buttons that **toggle** specific lights. The goal is to find the minimum number of button presses needed to configure all machines' indicator lights to their target patterns.

### Input Format

-   Each line represents one machine with three components:
-   `[indicator diagram]` - Shows target state where `.` is off and `#` is on
-   `(button,wiring,schematics)` - Multiple button definitions, each listing which light indices to toggle
-   `{joltage,requirements}` - Can be ignored in Part 1

### Key Rules

-   All indicator lights start in the **off** state
-   Pressing a button **toggles** (flips on/off) all lights listed in that button's schematic
-   Light indices are 0-based (0 = first light, 1 = second light, etc.)
-   Each button can be pressed any integer number of times (0, 1, 2, ...)
-   Goal: minimize total button presses across all machines

### Example

Input:

```
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
```

**Explanation:**

Machine 1: `[.##.]` has 4 lights, target is `[off, on, on, off]`

-   Available buttons: `(3)`, `(1,3)`, `(2)`, `(2,3)`, `(0,2)`, `(0,1)`
-   Optimal solution: Press `(0,2)` once and `(0,1)` once
    -   Start: `[0,0,0,0]`
    -   Press `(0,2)`: toggles lights 0 and 2 -> `[1,0,1,0]`
    -   Press `(0,1)`: toggles lights 0 and 1 -> `[0,1,1,0]`
-   Total: **2 presses**

Machine 2: `[...#.]` needs minimum **3 presses**

Machine 3: `[.###.#]` needs minimum **2 presses**

**Expected output:** 2 + 3 + 2 = **7**

### Idea

1. Parse each machine's target lights pattern and available buttons
2. Try all possible combinations of buttons (since each button pressed once toggles its lights)
3. For each combination, simulate the toggles and check if the result matches the target pattern
4. Return the minimum number of buttons (combination size) that achieves the target across all machines

## Part 2

Part 2 switches from configuring **indicator lights** to configuring **joltage counters**. Instead of toggling, buttons now **increment** specific counters. Each machine has counters (initially all zero) that must reach exact target values specified in the joltage requirements.

### Additional Rules

-   Ignore the indicator light diagrams `[...]`
-   Focus on joltage requirements `{num1,num2,...}` as target counter values
-   All counters start at **0**
-   Pressing a button **increments by 1** each counter listed in its schematic (no toggling)
-   Goal: minimize total button presses to reach exact joltage values

### Example

Using the same input:

```
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
```

**Explanation:**

Machine 1: Target counters `{3,5,4,7}` (4 counters)

-   Optimal: Press `(3)` 1x, `(1,3)` 3x, `(2,3)` 3x, `(0,2)` 1x, `(0,1)` 2x
-   Counter 0: `(0,2)` 1x + `(0,1)` 2x = 3 ✓
-   Counter 1: `(1,3)` 3x + `(0,1)` 2x = 5 ✓
-   Counter 2: `(2,3)` 3x + `(0,2)` 1x = 4 ✓
-   Counter 3: `(3)` 1x + `(1,3)` 3x + `(2,3)` 3x = 7 ✓
-   Total: **10 presses**

Machine 2: Minimum **12 presses**

Machine 3: Minimum **11 presses**

**Expected output:** 10 + 12 + 11 = **33**

### Important Edge Cases

-   Some buttons affect multiple counters simultaneously
-   Must find exact integer solutions (can't press a button fractional times)
-   This is a system of linear equations with non-negative integer constraints
-   Multiple button combinations may achieve targets, but only the minimum count matters

### Idea

1. Parse each machine's joltage requirements as target values and button schematics
2. Model as a linear programming problem: minimize sum of button presses
3. Create constraint matrix where each row represents a counter and columns represent buttons
4. Solve using integer linear programming with bounds (button presses >= 0) to find minimum total presses
